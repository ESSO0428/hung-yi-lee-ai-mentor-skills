import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "skills" / "hung-yi-ml-research-advisor" / "tools" / "triage.py"
sys.path.insert(0, str(TOOL.parent))

from triage import triage  # noqa: E402


def cls(**kw):
    return triage(kw)["classification"]


def run_cli(path):
    return subprocess.run(
        [sys.executable, str(TOOL), "--input", str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_refuses_without_train():
    r = triage({"val": 1.0})
    assert r["status"] == "refused" and r["classification"] == "insufficient_evidence"


def test_cli_refuses_with_exit_2(tmp_path):
    f = tmp_path / "x.json"
    f.write_text(json.dumps({"val": 1.0}))
    proc = run_cli(f)
    assert proc.returncode == 2
    assert json.loads(proc.stdout)["status"] == "refused"


def test_optimization_when_deeper_worse_and_nested():
    # lecture example: linear 71, deeper net about 80 -> optimization
    assert cls(train=80, shallow_baseline_train=71, nested=True) == "optimization"


def test_nested_unknown_blocks_optimization():
    assert cls(train=80, shallow_baseline_train=71) == "insufficient_evidence"
    assert cls(train=80, shallow_baseline_train=71, nested=False) == "insufficient_evidence"


def test_model_bias_when_train_short_of_target_but_not_worse_than_baseline():
    assert cls(train=60, shallow_baseline_train=71, train_target=30, nested=True) == "model_bias"


def test_train_bad_without_baseline_is_insufficient():
    assert cls(train=60, train_target=30) == "insufficient_evidence"


def test_overfitting_and_mismatch_split_on_distribution():
    base = dict(train=22, val=1300, train_target=30)
    assert cls(**base, distribution="same") == "overfitting"
    assert cls(**base, distribution="different") == "mismatch"
    assert cls(**base) == "insufficient_evidence"


def test_distribution_note_keywords():
    base = dict(train=71, val=122, train_target=100)
    assert cls(**base, distribution_note="train 2020, test 2021, different source") == "mismatch"
    assert cls(**base, distribution_note="random split, same source") == "overfitting"


def test_higher_is_better_direction():
    r = triage({"train": 0.99, "val": 0.6, "direction": "higher", "train_target": 0.9, "distribution": "same"})
    assert r["classification"] == "overfitting"
    r = triage({"train": 0.5, "shallow_baseline_train": 0.7, "direction": "higher", "nested": True})
    assert r["classification"] == "optimization"


def test_no_val_is_insufficient():
    assert cls(train=10, train_target=20) == "insufficient_evidence"


def test_no_problem_detected():
    assert cls(train=10, val=10.5, train_target=20) == "no_problem_detected"


def test_csv_input(tmp_path):
    f = tmp_path / "x.csv"
    f.write_text("train,val,train_target,distribution\n22,1300,30,same\n")
    proc = run_cli(f)
    assert proc.returncode == 0
    assert json.loads(proc.stdout)["classification"] == "overfitting"


def test_reasons_and_read_present():
    r = triage({"train": 80, "shallow_baseline_train": 71, "nested": True})
    assert r["reasons"] and r["read"] and r["next_experiment"]
