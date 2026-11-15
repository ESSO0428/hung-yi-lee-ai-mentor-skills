#!/usr/bin/env python3
"""Triage a failing run into optimization / model_bias / overfitting / mismatch.

Stdlib only. Follows references/skeleton.md: train metric first, shallow baseline
(with the nested-function-set precondition) to split bias from optimization,
then the train/val gap and data origin to split overfitting from mismatch.
Refuses to classify without a train metric (exit code 2).

Input: a JSON object or a one-row CSV with keys
  train (required), val, test, shallow_baseline_train, train_target,
  direction (lower|higher, default lower), nested (true|false|unknown),
  distribution (same|different|unknown), distribution_note (free text).
Command-line flags override file values.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

DEFAULT_GAP_REL = 0.25  # tool heuristic, NOT from the lectures
FIELDS_FLOAT = ("train", "val", "test", "shallow_baseline_train", "train_target")

DIFFERENT_WORDS = ("different", "shift", "mismatch", "not the same", "不同", "不一樣", "偏移", "換了")
SAME_WORDS = ("same", "iid", "random split", "相同", "同一", "隨機切")


def _to_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def _to_tristate(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"true", "yes", "1", "y"}:
        return True
    if text in {"false", "no", "0", "n"}:
        return False
    return None


def load_input(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".csv":
        rows = list(csv.DictReader(text.splitlines()))
        if len(rows) != 1:
            raise ValueError("CSV input must contain exactly one data row")
        return dict(rows[0])
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("JSON input must be an object")
    return data


def _distribution(payload: dict[str, Any]) -> str:
    raw = str(payload.get("distribution") or "").strip().lower()
    if raw in {"same", "different", "unknown"}:
        return raw
    note = str(payload.get("distribution_note") or "").lower()
    if note:
        if any(w in note for w in DIFFERENT_WORDS):
            return "different"
        if any(w in note for w in SAME_WORDS):
            return "same"
    return "unknown"


def triage(payload: dict[str, Any], gap_rel: float = DEFAULT_GAP_REL) -> dict[str, Any]:
    values = {k: _to_float(payload.get(k)) for k in FIELDS_FLOAT}
    direction = str(payload.get("direction") or "lower").lower()
    if direction not in {"lower", "higher"}:
        raise ValueError("direction must be 'lower' or 'higher'")
    nested = _to_tristate(payload.get("nested"))
    distribution = _distribution(payload)
    train, val, test = values["train"], values["val"], values["test"]
    baseline, target = values["shallow_baseline_train"], values["train_target"]

    result: dict[str, Any] = {
        "schema_version": "triage.v1",
        "direction": direction,
        "inputs": {**values, "nested": nested, "distribution": distribution},
        "gap_rel_threshold": gap_rel,
        "reasons": [],
        "unknowns": [],
        "read": [],
        "next_experiment": None,
    }
    reasons: list[str] = result["reasons"]
    unknowns: list[str] = result["unknowns"]

    if train is None:
        result.update(
            status="refused",
            classification="insufficient_evidence",
            next_experiment="先取得 training metric（同一個 metric、同一份 train 資料）；沒有 train loss 無法分辨 model bias、optimization、overfitting。",
        )
        reasons.append("沒有 train metric：不猜。第一問是「training loss 多少」。")
        result["read"].append("references/skeleton.md A1")
        return result

    def worse(a: float, b: float) -> bool:
        return a > b if direction == "lower" else a < b

    result["status"] = "ok"
    baseline_worse = baseline is not None and worse(train, baseline)
    train_fail = target is not None and worse(train, target)
    train_ok = target is not None and not train_fail

    if baseline_worse:
        reasons.append(f"train={train} 比淺模型基準 {baseline} 更差：更大的模型應至少做到淺模型的水準。")
        if nested is True:
            result["classification"] = "optimization"
            reasons.append("函式集合為巢狀（深模型包含淺模型），所以這是 optimization 沒做好，不是 model bias。")
            result["read"] += ["references/skeleton.md B1", "references/optimization.md 0"]
            result["next_experiment"] = "先調 lr、epoch、batch、optimizer 讓 train 至少追平淺模型基準；預期 train 追平後才有資格談 bias 或 overfitting。"
        else:
            result["classification"] = "insufficient_evidence"
            unknowns.append("巢狀前提未確認" if nested is None else "函式集合非巢狀，淺模型比較不成立")
            reasons.append("淺模型比較只在函式集合巢狀時成立（整理者推論的前提）；目前不能下 optimization 結論。")
            result["read"].append("references/skeleton.md B1")
            result["next_experiment"] = "確認大模型是否包含小模型（或改用同族、可巢狀的基準），再重做比較。"
        return result

    if train_fail:
        if baseline is not None:
            result["classification"] = "model_bias"
            reasons.append(
                f"train={train} 未達目標 {target}，但沒有比淺模型基準 {baseline} 差：候選是函式集合太小（針不在海裡），屬推論，需用容量實驗確認。"
            )
            result["read"] += ["references/skeleton.md B4", "references/optimization.md 0"]
            result["next_experiment"] = "加 features、加寬或加深一個級距；預期若是 model bias，train 會明顯下降。若 train 沒降，回頭查 optimization。"
        else:
            result["classification"] = "insufficient_evidence"
            unknowns.append("沒有淺模型基準，無法分 model bias 與 optimization")
            reasons.append(f"train={train} 未達目標 {target}，但缺淺模型基準：model bias 與 optimization 症狀相同、解法相反。")
            result["read"].append("references/skeleton.md B1")
            result["next_experiment"] = "跑一個淺模型或 linear 基準（確認巢狀關係），比較 train。"
        return result

    # train not shown to be failing
    if val is None:
        result["classification"] = "insufficient_evidence"
        unknowns.append("沒有 val metric")
        if not train_ok and baseline is None:
            unknowns.append("train 好不好無參照（課程沒給門檻）")
        reasons.append("train 沒有被證明有問題，但缺 val：無法談 overfitting／mismatch。")
        result["read"].append("references/skeleton.md A")
        result["next_experiment"] = "提供 val metric（同 metric）；若 train 好壞無參照，再給 train_target 或淺模型基準。"
        return result

    gap_abs = (val - train) if direction == "lower" else (train - val)
    rel = gap_abs / max(abs(train), 1e-12)
    result["gap"] = {"absolute": gap_abs, "relative_to_train": rel}
    if rel >= gap_rel:
        reasons.append(f"val 比 train 差 {gap_abs:.4g}（相對 {rel:.0%}，超過工具啟發式門檻 {gap_rel:.0%}；門檻不是課程數字）。")
        if not train_ok and baseline is None:
            unknowns.append("train 本身好不好未判斷")
        if distribution == "different":
            result["classification"] = "mismatch"
            reasons.append("train 與 val/test 的產生方式不同：這是 mismatch，加訓練資料沒用。")
            result["read"] += ["references/generalization-shift.md A", "references/generalization-shift.md B"]
            result["next_experiment"] = "量兩個數字夾住問題：source→target 與 target→target；再依對 target 的了解選方法（改切分、換資料、adaptation）。"
        elif distribution == "same":
            result["classification"] = "overfitting"
            reasons.append("train 與 val 同來源：train 好、val 差才叫 overfitting。")
            result["read"] += ["references/skeleton.md C1", "references/generalization-shift.md F"]
            result["next_experiment"] = "加真實資料（或合理 augmentation）；預期 gap 縮小、train 略升。限制彈性要小心別退回 bias。"
        else:
            result["classification"] = "insufficient_evidence"
            unknowns.append("train 與 val/test 的產生方式是否相同")
            reasons.append("gap 大，但 overfitting 與 mismatch 要靠「對資料產生方式的理解」區分，課程沒給統計檢定。")
            result["read"].append("references/generalization-shift.md A")
            result["next_experiment"] = "確認時間、來源、批次、設備是否一致；畫 val 殘差是否系統性偏一邊，再決定走 overfitting 或 mismatch 處方。"
    elif train_ok:
        result["classification"] = "no_problem_detected"
        reasons.append("train 達目標且 val 沒有明顯落差（以工具啟發式門檻判斷）。")
    else:
        result["classification"] = "insufficient_evidence"
        unknowns.append("train 好壞無參照（沒有 train_target，也沒有淺模型基準顯示更差）")
        reasons.append("train 與 val 沒有明顯落差，但 train 本身可能仍不夠好。")
        result["read"].append("references/skeleton.md B1")
        result["next_experiment"] = "提供 train_target 或跑淺模型基準。"

    if test is not None and worse(test, val):
        t_gap = abs(test - val) / max(abs(val), 1e-12)
        if t_gap >= gap_rel:
            reasons.append(f"test 比 val 差 {t_gap:.0%}：檢查 val 是否被反覆用來選模（驗證集也會被用壞）或 test 分佈不同。")
            result["read"].append("references/skeleton.md D3")
    return result


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--input", type=Path, help="JSON or one-row CSV")
    for name in FIELDS_FLOAT:
        p.add_argument(f"--{name.replace('_', '-')}", type=float)
    p.add_argument("--direction", choices=("lower", "higher"))
    p.add_argument("--nested", choices=("true", "false", "unknown"))
    p.add_argument("--distribution", choices=("same", "different", "unknown"))
    p.add_argument("--distribution-note")
    p.add_argument("--gap-rel", type=float, default=DEFAULT_GAP_REL)
    p.add_argument("--json", action="store_true", help="accepted for symmetry; output is always JSON")
    args = p.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    payload: dict[str, Any] = {}
    if args.input:
        try:
            payload = load_input(args.input)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False))
            return 1
    for key in (*FIELDS_FLOAT, "direction", "nested", "distribution", "distribution_note"):
        value = getattr(args, key)
        if value is not None:
            payload[key] = value
    try:
        result = triage(payload, args.gap_rel)
    except (ValueError, TypeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result.get("status") == "refused" else 0


if __name__ == "__main__":
    sys.exit(main())
