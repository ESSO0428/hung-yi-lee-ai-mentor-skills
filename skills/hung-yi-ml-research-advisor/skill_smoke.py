#!/usr/bin/env python3
"""Run a read-only smoke check against an isolated copy of the Advisor Skill."""

from __future__ import annotations

import argparse
import json
import hashlib
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any

from bootstrap import bootstrap


def _ignore_local_runtime(_path: str, names: list[str]) -> set[str]:
    """Keep smoke copies focused on skill sources, not a local installed venv."""

    return {name for name in names if name in {".venv", "__pycache__"}}


def _torch_runtime_smoke(skill_root: Path) -> dict[str, Any]:
    """Exercise diagnostics when the canonical torch extra is installed."""

    try:
        import torch
    except ImportError:
        return {"status": "SKIPPED_DEPENDENCY", "reason": "torch extra is not installed"}
    path = skill_root / "tools" / "torch_diagnostics.py"
    spec = importlib.util.spec_from_file_location("mentor_torch_diagnostics", path)
    if spec is None or spec.loader is None:
        return {"status": "FAIL", "reason": "unable to load torch_diagnostics.py"}
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    model = torch.nn.Sequential(torch.nn.Linear(3, 4), torch.nn.ReLU(), torch.nn.Linear(4, 2))
    diagnostics = module.TorchDiagnostics(model)
    diagnostics.attach_activation_hooks()
    model(torch.ones(2, 3)).sum().backward()
    snapshot = diagnostics.snapshot()
    diagnostics.close()
    passed = (
        snapshot.get("parameter_count") == 26
        and snapshot.get("trainable_parameter_count") == 26
        and len(snapshot.get("activations", {})) == 3
        and any(row.get("gradient") for row in snapshot.get("parameters", []))
    )
    return {
        "status": "PASS" if passed else "FAIL",
        "parameter_count": snapshot.get("parameter_count"),
        "activation_count": len(snapshot.get("activations", {})),
    }


def _response_validator_smoke(isolated: Path, temp: str | Path) -> dict[str, Any]:
    """Exercise the advisor response contract in the isolated copy."""
    response_path = Path(temp) / "advisor-response.json"
    response_path.write_text(
        json.dumps(
            {
                "observations": [{"text": "validation loss is flat", "evidence_ids": ["m1"]}],
                "unknowns": ["split stability"],
                "hypotheses": [
                    {
                        "id": "capacity",
                        "claim": "capacity may be limiting",
                        "supporting_evidence": ["m1"],
                        "weakening_evidence": ["UNKNOWN"],
                        "discriminating_experiment": "run an ablation",
                    },
                    {
                        "id": "data",
                        "claim": "data may be limiting",
                        "supporting_evidence": ["UNKNOWN"],
                        "weakening_evidence": ["m1"],
                        "discriminating_experiment": "audit the split",
                    },
                ],
                "principles": [{"id": "MLRA-P0-001", "evidence_class": "DIRECT", "source_refs": ["m1"]}],
                "experiment": {
                    "fixed_conditions": "same split",
                    "primary_variable": "capacity",
                    "prediction": "validation improves",
                    "falsifier": "no improvement",
                    "cost_or_risk": "three runs",
                },
                "recommendation": {
                    "next_action": "run the ablation",
                    "confidence": 0.6,
                    "reasoning_mode": "SOURCE_GROUNDED",
                    "belief_update": "update after validation result",
                },
                "provenance": [{"evidence_id": "m1", "source": "metrics.csv", "locator": "row=1"}],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            sys.executable,
            str(isolated / "tools" / "response_validator.py"),
            "--input",
            str(response_path),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    payload: dict[str, Any] = {}
    if result.returncode == 0:
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            payload = {}
    return {
        "status": "PASS"
        if result.returncode == 0 and payload.get("status") == "PASS"
        else "FAIL",
        "schema_version": payload.get("schema_version"),
        "errors": payload.get("errors", []),
        "returncode": result.returncode,
        "stderr": result.stderr[-500:],
        "response_path": str(response_path),
    }


def _advisor_provenance_smoke(isolated: Path, response_runtime: dict[str, Any], knowledge: Path | None) -> dict[str, Any]:
    """Exercise the response-to-normalized-knowledge provenance gate."""
    if knowledge is None:
        return {"status": "SKIPPED_INPUT", "reason": "normalized knowledge was not supplied"}
    result = subprocess.run(
        [
            sys.executable,
            str(isolated / "tools" / "advisor_provenance_audit.py"),
            "--response",
            response_runtime["response_path"],
            "--knowledge",
            str(knowledge),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    payload: dict[str, Any] = {}
    if result.returncode == 0:
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            payload = {}
    return {
        "status": "PASS"
        if result.returncode == 0 and payload.get("status") == "PASS"
        else "FAIL",
        "schema_version": payload.get("schema_version"),
        "errors": payload.get("errors", []),
        "returncode": result.returncode,
        "principles_checked": payload.get("principles_checked"),
        "stderr": result.stderr[-500:],
    }


def _mentor_response_gate_smoke(isolated: Path, response_runtime: dict[str, Any], knowledge: Path | None) -> dict[str, Any]:
    """Exercise the one-command response contract plus provenance gate."""
    if knowledge is None:
        return {"status": "SKIPPED_INPUT", "reason": "normalized knowledge was not supplied"}
    result = subprocess.run(
        [
            sys.executable,
            str(isolated / "tools" / "mentor_response_gate.py"),
            "--response",
            response_runtime["response_path"],
            "--knowledge",
            str(knowledge),
            "--json",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    payload: dict[str, Any] = {}
    if result.returncode == 0:
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            payload = {}
    return {
        "status": "PASS"
        if result.returncode == 0 and payload.get("status") == "PASS"
        else "FAIL",
        "schema_version": payload.get("schema_version"),
        "errors": payload.get("errors", []),
        "returncode": result.returncode,
        "response_validation": payload.get("response_validation", {}).get("status"),
        "provenance_audit": payload.get("provenance_audit", {}).get("status"),
        "stderr": result.stderr[-500:],
    }


def _source_files(root: Path) -> list[str]:
    return sorted(
        str(path.relative_to(root))
        for path in root.rglob("*")
        if path.is_file() and ".venv" not in path.parts and "__pycache__" not in path.parts and path.suffix != ".pyc"
    )


def _source_fingerprint(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".venv" in path.parts or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def run_smoke(skill_root: Path, knowledge: Path | None = None) -> dict[str, Any]:
    source_skill = skill_root.resolve()
    source_knowledge = knowledge.resolve() if knowledge else None
    with tempfile.TemporaryDirectory(prefix="mlra-skill-smoke-") as temp:
        isolated = Path(temp) / "skill"
        shutil.copytree(source_skill, isolated, ignore=_ignore_local_runtime)
        isolated_knowledge: Path | None = None
        if source_knowledge is not None:
            isolated_knowledge = Path(temp) / "normalized_principles.json"
            shutil.copy2(source_knowledge, isolated_knowledge)

        before_skill = _source_files(isolated)
        result = bootstrap(isolated, isolated_knowledge)
        recipe_input = Path(temp) / "recipe-metrics.csv"
        recipe_input.write_text(
            "run_id,step,split,metric,value\nsmoke,1,validation,loss,1.0\nsmoke,2,validation,loss,0.5\n",
            encoding="utf-8",
        )
        recipe_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "recipe_tools.py"),
                "summarize-metrics",
                "--input",
                str(recipe_input),
                "--objective",
                '{"validation/loss":"min"}',
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        recipe_payload: dict[str, Any] = {}
        if recipe_result.returncode == 0:
            try:
                recipe_payload = json.loads(recipe_result.stdout)
            except json.JSONDecodeError:
                recipe_payload = {}
        split_input = Path(temp) / "split-audit.csv"
        split_input.write_text(
            "sample_id,split,group_id,content_hash,label\n"
            "a,train,g1,h1,cat\n"
            "b,train,g2,h2,dog\n"
            "c,validation,g3,h3,cat\n"
            "d,validation,g4,h4,dog\n",
            encoding="utf-8",
        )
        split_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "dataset_split_audit.py"),
                "--input",
                str(split_input),
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        split_payload: dict[str, Any] = {}
        if split_result.returncode == 0:
            try:
                split_payload = json.loads(split_result.stdout)
            except json.JSONDecodeError:
                split_payload = {}
        split_ok = split_result.returncode == 0 and split_payload.get("status") == "PASS"
        evaluation_input = Path(temp) / "evaluation-predictions.json"
        evaluation_input.write_text(
            json.dumps(
                [
                    {"label": 1, "prediction": 1, "score": 0.9, "slice": "a"},
                    {"label": 1, "prediction": 0, "score": 0.4, "slice": "a"},
                    {"label": 0, "prediction": 0, "score": 0.2, "slice": "b"},
                    {"label": 0, "prediction": 1, "score": 0.7, "slice": "b"},
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        evaluation_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "model_evaluation.py"),
                "classification",
                "--input",
                str(evaluation_input),
                "--score-column",
                "score",
                "--group-by",
                "slice",
                "--resamples",
                "100",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        evaluation_payload: dict[str, Any] = {}
        if evaluation_result.returncode == 0:
            try:
                evaluation_payload = json.loads(evaluation_result.stdout)
            except json.JSONDecodeError:
                evaluation_payload = {}
        evaluation_ok = (
            evaluation_result.returncode == 0
            and evaluation_payload.get("schema_version") == "model-evaluation.v1"
            and evaluation_payload.get("metrics", {}).get("brier_score") is not None
            and evaluation_payload.get("calibration", {}).get("expected_calibration_error") is not None
            and len(evaluation_payload.get("groups", [])) == 2
        )
        multiclass_input = Path(temp) / "evaluation-multiclass.json"
        multiclass_input.write_text(
            json.dumps(
                [
                    {"label": "cat", "prediction": "cat", "slice": "a"},
                    {"label": "cat", "prediction": "dog", "slice": "a"},
                    {"label": "dog", "prediction": "dog", "slice": "b"},
                    {"label": "bird", "prediction": "dog", "slice": "b"},
                    {"label": "bird", "prediction": "bird", "slice": "b"},
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        multiclass_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "model_evaluation.py"),
                "classification",
                "--input",
                str(multiclass_input),
                "--group-by",
                "slice",
                "--resamples",
                "100",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        multiclass_payload: dict[str, Any] = {}
        if multiclass_result.returncode == 0:
            try:
                multiclass_payload = json.loads(multiclass_result.stdout)
            except json.JSONDecodeError:
                multiclass_payload = {}
        multiclass_ok = (
            multiclass_result.returncode == 0
            and multiclass_payload.get("task") == "multiclass_classification"
            and multiclass_payload.get("metrics", {}).get("macro_f1") is not None
            and multiclass_payload.get("metrics", {}).get("balanced_accuracy") is not None
            and len(multiclass_payload.get("groups", [])) == 2
        )
        regression_input = Path(temp) / "evaluation-regression.json"
        regression_input.write_text(
            json.dumps(
                [
                    {"label": 1.0, "prediction": 1.5, "slice": "a"},
                    {"label": 2.0, "prediction": 1.0, "slice": "a"},
                    {"label": 3.0, "prediction": 2.5, "slice": "b"},
                    {"label": 4.0, "prediction": 5.0, "slice": "b"},
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        regression_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "model_evaluation.py"),
                "regression",
                "--input",
                str(regression_input),
                "--group-by",
                "slice",
                "--resamples",
                "100",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        regression_payload: dict[str, Any] = {}
        if regression_result.returncode == 0:
            try:
                regression_payload = json.loads(regression_result.stdout)
            except json.JSONDecodeError:
                regression_payload = {}
        regression_ok = (
            regression_result.returncode == 0
            and regression_payload.get("task") == "regression"
            and regression_payload.get("metrics", {}).get("mae") is not None
            and regression_payload.get("metrics", {}).get("rmse") is not None
            and len(regression_payload.get("groups", [])) == 2
        )
        ranking_input = Path(temp) / "evaluation-ranking.json"
        ranking_input.write_text(
            json.dumps(
                [
                    {"query_id": "q1", "rank": 1, "relevance": 1, "slice": "a"},
                    {"query_id": "q1", "rank": 2, "relevance": 0, "slice": "a"},
                    {"query_id": "q2", "rank": 1, "relevance": 0, "slice": "b"},
                    {"query_id": "q2", "rank": 2, "relevance": 1, "slice": "b"},
                ],
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        ranking_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "model_evaluation.py"),
                "ranking",
                "--input",
                str(ranking_input),
                "--group-by",
                "slice",
                "--k",
                "2",
                "--resamples",
                "100",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        ranking_payload: dict[str, Any] = {}
        if ranking_result.returncode == 0:
            try:
                ranking_payload = json.loads(ranking_result.stdout)
            except json.JSONDecodeError:
                ranking_payload = {}
        ranking_ok = (
            ranking_result.returncode == 0
            and ranking_payload.get("task") == "ranked_retrieval"
            and ranking_payload.get("metrics", {}).get("mrr") == 0.75
            and ranking_payload.get("metrics", {}).get("recall_at_k") == 1.0
            and len(ranking_payload.get("groups", [])) == 2
        )
        ffp_artifact = Path(temp) / "ffp-metrics.csv"
        ffp_artifact.write_text("MRR_F,MRR_M\n0.6489,0.6994\n", encoding="utf-8")
        ffp_input = Path(temp) / "ffp-input.json"
        ffp_input.write_text(
            json.dumps(
                {
                    "schema_version": "ffp-evaluation-input.v1",
                    "project_id": "FFP",
                    "required_versions": ["FFP", "FFP_simple", "FFP_new_mlp"],
                    "artifacts": [
                        {
                            "artifact_id": "metrics-ffp",
                            "kind": "metrics",
                            "version": "FFP",
                            "path": str(ffp_artifact),
                            "sha256": hashlib.sha256(ffp_artifact.read_bytes()).hexdigest(),
                        }
                    ],
                    "transitions": [
                        {
                            "transition_id": "FFP_to_FFP_simple",
                            "from_version": "FFP",
                            "to_version": "FFP_simple",
                            "observed": {"evidence_ids": ["metrics-ffp"]},
                            "actual_outcome": {"next_mrr": 0.70},
                        }
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        ffp_audit_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "ffp_evaluation.py"),
                "audit",
                "--input",
                str(ffp_input),
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        ffp_audit_payload: dict[str, Any] = {}
        if ffp_audit_result.returncode == 0:
            try:
                ffp_audit_payload = json.loads(ffp_audit_result.stdout)
            except json.JSONDecodeError:
                ffp_audit_payload = {}
        ffp_blind_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "ffp_evaluation.py"),
                "blind-pack",
                "--input",
                str(ffp_input),
                "--transition-id",
                "FFP_to_FFP_simple",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        ffp_blind_payload: dict[str, Any] = {}
        if ffp_blind_result.returncode == 0:
            try:
                ffp_blind_payload = json.loads(ffp_blind_result.stdout)
            except json.JSONDecodeError:
                ffp_blind_payload = {}
        ffp_ok = (
            ffp_audit_result.returncode == 0
            and ffp_audit_payload.get("status") == "INPUT_MISSING"
            and ffp_audit_payload.get("artifacts", [{}])[0].get("status") == "VERIFIED"
            and ffp_blind_result.returncode == 0
            and ffp_blind_payload.get("status") == "READY_FOR_ADVICE"
            and ffp_blind_payload.get("leakage_check", {}).get("post_transition_outcome_withheld") is True
            and ffp_blind_payload.get("leakage_check", {}).get("future_fields_removed") == ["actual_outcome"]
        )
        advanced_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "advanced_recipe_tools.py"),
                "dependencies",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        advanced_payload: dict[str, Any] = {}
        if advanced_result.returncode == 0:
            try:
                advanced_payload = json.loads(advanced_result.stdout)
            except json.JSONDecodeError:
                advanced_payload = {}
        advanced_ok = (
            advanced_result.returncode == 0
            and advanced_payload.get("schema_version") == "advanced-recipe-capabilities.v1"
            and set(advanced_payload.get("capabilities", {})) >= {"numpy", "pandas", "matplotlib", "torch"}
        )
        comparison_input = Path(temp) / "comparison.csv"
        comparison_input.write_text(
            "variant,seed,score\n"
            "baseline,1,0.60\n"
            "candidate,1,0.70\n"
            "baseline,2,0.50\n"
            "candidate,2,0.70\n",
            encoding="utf-8",
        )
        comparison_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "advanced_recipe_tools.py"),
                "compare-groups",
                "--input",
                str(comparison_input),
                "--group-column",
                "variant",
                "--value-column",
                "score",
                "--baseline",
                "baseline",
                "--candidate",
                "candidate",
                "--paired-column",
                "seed",
                "--resamples",
                "100",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        comparison_payload: dict[str, Any] = {}
        if comparison_result.returncode == 0:
            try:
                comparison_payload = json.loads(comparison_result.stdout)
            except json.JSONDecodeError:
                comparison_payload = {}
        comparison_ok = (
            comparison_result.returncode == 0
            and comparison_payload.get("comparison") == "candidate_minus_baseline"
            and comparison_payload.get("paired") is True
            and comparison_payload.get("n_pairs") == 2
        )
        visual_root = Path(temp) / "visual-evidence"
        visual_root.mkdir(parents=True, exist_ok=True)
        visual_frame = visual_root / "frame.jpg"
        visual_frame.write_bytes(b"mentor-smoke-frame")
        visual_digest = hashlib.sha256(visual_frame.read_bytes()).hexdigest()
        visual_manifest = visual_root / "video.json"
        visual_manifest.write_text(
            json.dumps(
                {
                    "schema_version": "visual-evidence.v1",
                    "video_id": "smoke-video",
                    "provenance": {"source_url": "https://www.youtube.com/watch?v=smoke-video"},
                    "frames": [
                        {
                            "request_id": "smoke-request",
                            "claim_id": "smoke-claim",
                            "timestamp_seconds": 10.0,
                            "frame_path": "visual-evidence/frame.jpg",
                            "frame_sha256": visual_digest,
                        }
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        visual_index = visual_root / "index.json"
        visual_index.write_text(
            json.dumps(
                {
                    "schema_version": "visual-evidence-index.v1",
                    "entries": [
                        {
                            "claim_id": "smoke-claim",
                            "video_id": "smoke-video",
                            "manifest_path": "visual-evidence/video.json",
                        }
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )
        visual_result = subprocess.run(
            [
                sys.executable,
                str(isolated / "tools" / "visual_evidence_lookup.py"),
                "--root",
                str(Path(temp)),
                "--index",
                str(visual_index),
                "--claim-id",
                "smoke-claim",
                "--json",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        visual_payload: dict[str, Any] = {}
        if visual_result.returncode == 0:
            try:
                visual_payload = json.loads(visual_result.stdout)
            except json.JSONDecodeError:
                visual_payload = {}
        visual_ok = (
            visual_result.returncode == 0
            and visual_payload.get("status") == "PASS"
            and visual_payload.get("match_count") == 1
            and visual_payload.get("integrity_failures") == 0
        )
        response_runtime = _response_validator_smoke(isolated, temp)
        provenance_runtime = _advisor_provenance_smoke(isolated, response_runtime, isolated_knowledge)
        response_gate_runtime = _mentor_response_gate_smoke(isolated, response_runtime, isolated_knowledge)
        torch_runtime = _torch_runtime_smoke(isolated)
        after_skill = _source_files(isolated)
        result.update(
            {
                "smoke": "PASS"
                if result["status"] == "PASS"
                and before_skill == after_skill
                and recipe_result.returncode == 0
                and split_ok
                and evaluation_ok
                and multiclass_ok
                and regression_ok
                and ranking_ok
                and ffp_ok
                and advanced_ok
                and comparison_ok
                and visual_ok
                and response_runtime["status"] == "PASS"
                and provenance_runtime["status"] in {"PASS", "SKIPPED_INPUT"}
                and response_gate_runtime["status"] in {"PASS", "SKIPPED_INPUT"}
                and torch_runtime["status"] in {"PASS", "SKIPPED_DEPENDENCY"}
                and recipe_payload.get("summaries", [{}])[0].get("best_value") == 0.5
                else "FAIL",
                "isolated_copy": True,
                "source_skill": str(source_skill),
                "source_knowledge": str(source_knowledge) if source_knowledge else None,
                "source_fingerprint": _source_fingerprint(source_skill),
                "writes_sources": False,
                "isolated_files_unchanged": before_skill == after_skill,
                "recipe_tool": "PASS"
                if recipe_result.returncode == 0
                and recipe_payload.get("summaries", [{}])[0].get("best_value") == 0.5
                else "FAIL",
                "dataset_split_audit": "PASS" if split_ok else "FAIL",
                "model_evaluation": "PASS" if evaluation_ok else "FAIL",
                "model_evaluation_runtime": evaluation_payload,
                "multiclass_evaluation": "PASS" if multiclass_ok else "FAIL",
                "multiclass_evaluation_runtime": multiclass_payload,
                "regression_evaluation": "PASS" if regression_ok else "FAIL",
                "regression_evaluation_runtime": regression_payload,
                "ranking_evaluation": "PASS" if ranking_ok else "FAIL",
                "ranking_evaluation_runtime": ranking_payload,
                "ffp_evaluation": "PASS" if ffp_ok else "FAIL",
                "ffp_evaluation_runtime": {
                    "audit": ffp_audit_payload,
                    "blind_pack": ffp_blind_payload,
                    "data_status": ffp_audit_payload.get("status"),
                },
                "advanced_tool": "PASS" if advanced_ok else "FAIL",
                "advanced_comparison": "PASS" if comparison_ok else "FAIL",
                "visual_evidence_lookup": "PASS" if visual_ok else "FAIL",
                "response_validator": response_runtime["status"],
                "response_validator_runtime": response_runtime,
                "advisor_provenance_audit": provenance_runtime["status"],
                "advisor_provenance_runtime": provenance_runtime,
                "mentor_response_gate": response_gate_runtime["status"],
                "mentor_response_gate_runtime": response_gate_runtime,
                "advanced_capabilities": advanced_payload.get("capabilities", {}),
                "advanced_profiles": advanced_payload.get("profiles", {}),
                "torch_runtime": torch_runtime,
            }
        )
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).parent)
    parser.add_argument("--knowledge", type=Path)
    parser.add_argument("--output", type=Path, help="write the machine-readable smoke report to this path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = run_smoke(args.skill_root, args.knowledge)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{result['smoke']}: isolated Advisor Skill smoke")
    return 0 if result["smoke"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
