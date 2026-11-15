#!/usr/bin/env python3
"""Report which mentor evidence and diagnostic branches are usable.

This is a read-only router aid.  It does not download, parse, distill, or
upgrade evidence; it makes missing host inputs explicit before an advisor
answer is attempted.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


SCHEMA_VERSION = "mentor-capability-probe.v1"
DISTILLY_CONTEXT_SCHEMA = "hung-yi-distilly-p0-context.v1"
DISTILLY_CONTEXT_CLASSIFICATION = "SUPPLEMENTAL_RESEARCH_CONTEXT_NOT_FORMAL"
DISTILLY_CONTEXT_MATERIAL_IDS = ("p0_dossier", "p0_merged_summary")
DISTILLY_CONTEXT_CANDIDATE_FAMILIES = ("P1", "P2", "P3")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _resolve_repo_root(skill_root: Path, explicit: Path | None) -> Path | None:
    if explicit is not None:
        return explicit.resolve()
    for ancestor in (skill_root.resolve(), *skill_root.resolve().parents):
        if (ancestor / "knowledge").is_dir() and (ancestor / "data").is_dir():
            return ancestor
    return None


def _read_index(path: Path, expected_prefix: str) -> dict[str, Any]:
    if not path.is_file():
        return {"status": "INPUT_MISSING", "path": str(path), "reason": "file not found"}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return {"status": "FAIL", "path": str(path), "reason": f"invalid JSON: {exc}"}
    if not isinstance(payload, dict) or not str(payload.get("schema_version", "")).startswith(expected_prefix):
        return {"status": "FAIL", "path": str(path), "reason": "unexpected index schema"}
    counts = {
        key: len(value)
        for key, value in payload.items()
        if key in {"entries", "frames", "chunks", "assets"} and isinstance(value, list)
    }
    return {
        "status": "READY",
        "path": str(path),
        "schema_version": payload.get("schema_version"),
        "sha256": _sha256(path),
        "counts": counts,
    }


def _course_material_status(repo_root: Path | None) -> dict[str, Any]:
    if repo_root is None:
        return {"status": "INPUT_MISSING", "reason": "host repository root was not supplied"}
    manifest = repo_root / "data" / "manifest"
    for filename in (
        "course-material-source-index-crawl-latest.json",
        "course-material-source-index.json",
    ):
        result = _read_index(manifest / filename, "course-material-source-index.")
        if result["status"] == "READY":
            return result
    return {
        "status": "INPUT_MISSING",
        "path": str(manifest),
        "reason": "no verified course-material source index found",
    }


def _source_provenance_status(repo_root: Path | None, knowledge: Path | None) -> dict[str, Any]:
    """Check every normalized principle against the full repo evidence chain."""

    if repo_root is None or knowledge is None:
        return {
            "status": "INPUT_MISSING",
            "reason": "host repository root and normalized knowledge are required",
        }
    manifest_path = repo_root / "data" / "manifest" / "videos.json"
    source_dir = repo_root / "data" / "processing" / "source_chunks"
    audit_path = repo_root / "ml_research_advisor" / "provenance_audit.py"
    missing = [str(path) for path in (manifest_path, source_dir, audit_path) if not path.exists()]
    if missing or not knowledge.is_file():
        return {
            "status": "INPUT_MISSING",
            "reason": "required provenance inputs are missing",
            "missing": [*missing, *([str(knowledge)] if not knowledge.is_file() else [])],
        }
    try:
        normalized = json.loads(knowledge.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(normalized, dict) or not isinstance(normalized.get("principles"), list):
            raise ValueError("knowledge JSON must contain a principles list")
        if not isinstance(manifest, dict) or not isinstance(manifest.get("videos"), dict):
            raise ValueError("video manifest must contain a videos object")
        chunks_by_video: dict[str, dict[str, Any]] = {}
        chunk_files = sorted(source_dir.glob("*.json"))
        for path in chunk_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            video_id = payload.get("video_id") if isinstance(payload, dict) else None
            if isinstance(video_id, str) and video_id:
                chunks_by_video[video_id] = payload
        audit = _load_module(audit_path, "mentor_provenance_probe")
        report = audit.audit_principle_sample(
            normalized,
            manifest["videos"],
            chunks_by_video,
            sample_size=len(normalized["principles"]),
            seed=20260917,
        )
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError, ImportError) as exc:
        return {"status": "FAIL", "reason": f"provenance audit failed: {exc}"}
    summary = report.get("summary", {})
    failed = int(summary.get("failed", 0) or 0)
    return {
        "status": "READY" if failed == 0 else "FAIL",
        "manifest_path": str(manifest_path),
        "manifest_sha256": _sha256(manifest_path),
        "source_chunks_dir": str(source_dir),
        "source_chunk_file_count": len(chunk_files),
        "knowledge_path": str(knowledge),
        "knowledge_sha256": _sha256(knowledge),
        "summary": summary,
        "failed_principles": [
            item.get("principle_id")
            for item in report.get("items", [])
            if isinstance(item, dict) and item.get("status") != "PASS"
        ],
    }


def _visual_status(repo_root: Path | None) -> dict[str, dict[str, Any]]:
    names = {
        "video": "visual-evidence/index.json",
        "course_material": "course-material-visual-evidence/index.json",
    }
    if repo_root is None:
        return {
            key: {"status": "INPUT_MISSING", "reason": "host repository root was not supplied"}
            for key in names
        }
    base = repo_root / "data" / "processing"
    return {key: _read_index(base / relative, "") for key, relative in names.items()}


def _distilly_p0_context(
    skill_root: Path,
    repo_root: Path | None,
    knowledge: Path | None,
) -> dict[str, Any]:
    """Expose optional P0 research context without treating it as knowledge."""

    context_path = skill_root / "references" / "distilly-p0-context.json"
    if repo_root is None or knowledge is None or not knowledge.is_file():
        return {
            "status": "INPUT_MISSING",
            "path": str(context_path),
            "reason": "host repository root and normalized P0 knowledge are required",
        }
    if not context_path.is_file():
        return {
            "status": "INPUT_MISSING",
            "path": str(context_path),
            "reason": "P0 Distilly context manifest is missing",
        }
    try:
        context = json.loads(context_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        return {"status": "FAIL", "path": str(context_path), "reason": f"invalid JSON: {exc}"}
    if not isinstance(context, dict) or context.get("schema_version") != DISTILLY_CONTEXT_SCHEMA:
        return {"status": "FAIL", "path": str(context_path), "reason": "unexpected context schema"}
    if context.get("classification") != DISTILLY_CONTEXT_CLASSIFICATION:
        return {"status": "FAIL", "path": str(context_path), "reason": "context classification is not non-formal"}
    if tuple(context.get("candidate_families_not_formal", ())) != DISTILLY_CONTEXT_CANDIDATE_FAMILIES:
        return {"status": "FAIL", "path": str(context_path), "reason": "candidate families must remain non-formal"}

    formal_relative = context.get("formal_knowledge_path")
    if not isinstance(formal_relative, str):
        return {"status": "FAIL", "path": str(context_path), "reason": "formal knowledge path is invalid"}
    formal_relative_path = Path(formal_relative)
    if formal_relative_path.is_absolute() or ".." in formal_relative_path.parts:
        return {"status": "FAIL", "path": str(context_path), "reason": "formal knowledge path must stay inside the repository"}
    formal_path = repo_root / formal_relative_path
    if not formal_path.is_file() or knowledge.resolve() != formal_path.resolve():
        return {
            "status": "INPUT_MISSING",
            "path": str(context_path),
            "reason": "configured P0 knowledge source is unavailable or does not match the selected knowledge layer",
        }
    try:
        normalized = json.loads(knowledge.read_text(encoding="utf-8"))
        actual_ids = [item["id"] for item in normalized["principles"]]
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        return {"status": "FAIL", "path": str(context_path), "reason": f"cannot read normalized P0 IDs: {exc}"}
    expected_ids = context.get("formal_principle_ids")
    if not isinstance(expected_ids, list) or expected_ids != actual_ids:
        return {"status": "FAIL", "path": str(context_path), "reason": "context P0 IDs do not exactly match normalized knowledge"}

    configured_materials = context.get("materials")
    if not isinstance(configured_materials, list) or tuple(item.get("id") for item in configured_materials if isinstance(item, dict)) != DISTILLY_CONTEXT_MATERIAL_IDS:
        return {"status": "FAIL", "path": str(context_path), "reason": "context must contain only the two approved P0 materials"}
    materials: list[dict[str, Any]] = []
    missing: list[str] = []
    for item in configured_materials:
        if not isinstance(item, dict) or not isinstance(item.get("repo_relative_path"), str):
            return {"status": "FAIL", "path": str(context_path), "reason": "context material path is invalid"}
        relative = Path(item["repo_relative_path"])
        if relative.is_absolute() or ".." in relative.parts:
            return {"status": "FAIL", "path": str(context_path), "reason": "context material path must stay inside the repository"}
        material_path = repo_root / relative
        if not material_path.is_file():
            missing.append(str(material_path))
            continue
        materials.append(
            {
                "id": item["id"],
                "path": str(material_path),
                "sha256": _sha256(material_path),
                "purpose": item.get("purpose"),
            }
        )
    if missing:
        return {
            "status": "INPUT_MISSING",
            "path": str(context_path),
            "reason": "configured P0 research context is unavailable",
            "missing": missing,
        }
    return {
        "status": "READY",
        "path": str(context_path),
        "sha256": _sha256(context_path),
        "classification": DISTILLY_CONTEXT_CLASSIFICATION,
        "formal_knowledge": str(formal_path),
        "formal_principle_ids": expected_ids,
        "candidate_families_not_formal": list(DISTILLY_CONTEXT_CANDIDATE_FAMILIES),
        "materials": materials,
    }


def probe(
    *,
    skill_root: Path,
    repo_root: Path | None = None,
    knowledge: Path | None = None,
) -> dict[str, Any]:
    skill_root = skill_root.resolve()
    repo_root = _resolve_repo_root(skill_root, repo_root)
    if knowledge is None and repo_root is not None:
        candidate = repo_root / "knowledge" / "normalized_principles.json"
        knowledge = candidate if candidate.is_file() else None

    bootstrap = _load_module(skill_root / "bootstrap.py", "mentor_bootstrap_probe")
    bootstrap_result = bootstrap.bootstrap(skill_root, knowledge, require_knowledge=False)
    advanced = _load_module(skill_root / "tools" / "advanced_recipe_tools.py", "mentor_advanced_probe")
    dependency_result = advanced.dependency_report()
    course_materials = _course_material_status(repo_root)
    source_provenance = _source_provenance_status(repo_root, knowledge)
    visual_evidence = _visual_status(repo_root)
    distilly_p0_context = _distilly_p0_context(skill_root, repo_root, knowledge)

    source_ready = bool(bootstrap_result.get("source_grounded_ready"))
    issues: list[str] = []
    if not source_ready:
        issues.append("source_grounded:INPUT_MISSING")
    if course_materials.get("status") != "READY":
        issues.append(f"course_materials:{course_materials.get('status')}")
    if source_provenance.get("status") != "READY":
        issues.append(f"source_provenance:{source_provenance.get('status')}")
    if distilly_p0_context.get("status") != "READY":
        issues.append(f"distilly_p0_context:{distilly_p0_context.get('status')}")
    for name, status in visual_evidence.items():
        if status.get("status") != "READY":
            issues.append(f"visual_evidence.{name}:{status.get('status')}")
    for name in ("analysis", "torch", "all"):
        profile = dependency_result.get("profiles", {}).get(name, {})
        if profile.get("status") != "READY":
            issues.append(f"profile.{name}:{profile.get('status', 'INPUT_MISSING')}")
    status = "READY" if not issues else "READY_WITH_GAPS" if source_ready else "INPUT_MISSING"
    return {
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "skill_root": str(skill_root),
        "repo_root": str(repo_root) if repo_root else None,
        "source_grounded": {
            "status": bootstrap_result.get("status"),
            "ready": source_ready,
            "knowledge_status": bootstrap_result.get("knowledge_status"),
            "principle_count": bootstrap_result.get("principle_count", 0),
            "knowledge": bootstrap_result.get("knowledge"),
        },
        "course_materials": course_materials,
        "source_provenance": source_provenance,
        "distilly_p0_context": distilly_p0_context,
        "visual_evidence": visual_evidence,
        "profiles": dependency_result.get("profiles", {}),
        "tool_version": dependency_result.get("tool_version"),
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).parents[1])
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--knowledge", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = probe(skill_root=args.skill_root, repo_root=args.repo_root, knowledge=args.knowledge)
    except (OSError, ImportError, TypeError, ValueError, json.JSONDecodeError) as exc:
        result = {"schema_version": SCHEMA_VERSION, "status": "FAIL", "issues": [str(exc)]}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"{result['status']}: mentor capability probe")
        for issue in result.get("issues", []):
            print(f"- {issue}")
    return 0 if result["status"] in {"READY", "READY_WITH_GAPS", "INPUT_MISSING"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
