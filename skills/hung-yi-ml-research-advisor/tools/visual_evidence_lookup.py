"""Query and integrity-check stored visual evidence for mentor decisions.

The tool never downloads media or extracts new frames.  It resolves existing
video-frame and course-material visual indexes, filters them by a precise
claim/video/time/page selector, and verifies the referenced image hashes before
returning provenance that can be cited by the mentor skill.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


TOOL_VERSION = "1.0.0"
SCHEMA_VERSION = "visual-evidence-lookup.v1"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def _resolve(root: Path, raw: str | Path) -> Path:
    path = Path(raw)
    resolved = path if path.is_absolute() else root / path
    return resolved.resolve()


def _matches(
    item: dict[str, Any],
    *,
    claim_id: str | None,
    video_id: str | None,
    request_id: str | None,
    asset_id: str | None,
    page: int | None,
    timestamp: float | None,
    tolerance: float,
) -> bool:
    if claim_id and item.get("claim_id") != claim_id:
        return False
    if video_id and item.get("video_id") != video_id:
        return False
    if request_id and item.get("request_id") != request_id:
        return False
    if asset_id and item.get("asset_id") != asset_id:
        return False
    if page is not None and int(item.get("page", -1)) != page:
        return False
    if timestamp is not None:
        value = item.get("timestamp_seconds")
        if value is None or abs(float(value) - timestamp) > tolerance:
            return False
    return True


def _video_frames(root: Path, index_path: Path, index: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for entry in index.get("entries", []):
        if not isinstance(entry, dict):
            continue
        manifest_raw = entry.get("manifest_path")
        if not isinstance(manifest_raw, str):
            continue
        manifest_path = _resolve(root, manifest_raw)
        try:
            manifest = _load_json(manifest_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            yield {
                "index_path": str(index_path),
                "manifest_path": str(manifest_path),
                "manifest_error": str(exc),
                "claim_id": entry.get("claim_id"),
                "video_id": entry.get("video_id"),
            }
            continue
        provenance = manifest.get("provenance") if isinstance(manifest.get("provenance"), dict) else {}
        for frame in manifest.get("frames", []):
            if not isinstance(frame, dict):
                continue
            item = dict(frame)
            item.update(
                {
                    "evidence_kind": "video_frame",
                    "index_path": str(index_path),
                    "manifest_path": str(manifest_path),
                    "video_id": manifest.get("video_id", entry.get("video_id")),
                    "claim_id": frame.get("claim_id", entry.get("claim_id")),
                    "source_url": provenance.get("source_url"),
                }
            )
            yield item


def _course_images(root: Path, index_path: Path, index: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for entry in index.get("entries", []):
        if not isinstance(entry, dict):
            continue
        manifest_raw = entry.get("manifest_path")
        if not isinstance(manifest_raw, str):
            continue
        manifest_path = _resolve(root, manifest_raw)
        try:
            manifest = _load_json(manifest_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            yield {
                "index_path": str(index_path),
                "manifest_path": str(manifest_path),
                "manifest_error": str(exc),
                "asset_id": entry.get("asset_id"),
            }
            continue
        provenance = manifest.get("provenance") if isinstance(manifest.get("provenance"), dict) else {}
        for image in manifest.get("images", []):
            if not isinstance(image, dict):
                continue
            item = dict(image)
            item.update(
                {
                    "evidence_kind": "course_material_page",
                    "index_path": str(index_path),
                    "manifest_path": str(manifest_path),
                    "asset_id": manifest.get("asset_id", entry.get("asset_id")),
                    "course": manifest.get("course", entry.get("course")),
                    "course_year": manifest.get("course_year", entry.get("course_year")),
                    "row_context": manifest.get("row_context", entry.get("row_context")),
                    "source_url": manifest.get("source_url", entry.get("source_url")),
                    "source_page": provenance.get("source_page"),
                    "resolved_by_alternate": manifest.get("resolved_by_alternate", entry.get("resolved_by_alternate", False)),
                    "alternate_for_asset_id": manifest.get("alternate_for_asset_id", entry.get("alternate_for_asset_id")),
                }
            )
            yield item


def _integrity(root: Path, item: dict[str, Any]) -> dict[str, Any]:
    raw = item.get("frame_path") or item.get("image_path")
    if not isinstance(raw, str):
        return {"path_ok": False, "hash_ok": False, "integrity": "MISSING_PATH"}
    path = _resolve(root, raw)
    result: dict[str, Any] = {"path": str(path), "path_ok": path.is_file()}
    expected = item.get("frame_sha256") or item.get("sha256")
    if not path.is_file():
        result.update({"hash_ok": False, "integrity": "MISSING_FILE"})
        return result
    if not isinstance(expected, str) or not expected:
        result.update({"hash_ok": None, "integrity": "HASH_NOT_DECLARED"})
        return result
    try:
        actual = _sha256(path)
    except OSError as exc:
        result.update({"hash_ok": False, "integrity": "HASH_READ_ERROR", "error": str(exc)})
        return result
    result.update({"expected_sha256": expected, "actual_sha256": actual, "hash_ok": actual == expected})
    result["integrity"] = "PASS" if actual == expected else "HASH_MISMATCH"
    return result


def lookup(
    root: Path,
    *,
    indexes: list[Path] | None = None,
    claim_id: str | None = None,
    video_id: str | None = None,
    request_id: str | None = None,
    asset_id: str | None = None,
    page: int | None = None,
    timestamp: float | None = None,
    tolerance: float = 2.0,
) -> dict[str, Any]:
    root = Path(root).resolve()
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")
    if indexes:
        index_paths = [_resolve(root, path) for path in indexes]
    else:
        index_paths = [
            path
            for path in (
                root / "data" / "processing" / "visual-evidence" / "index.json",
                root / "data" / "processing" / "course-material-visual-evidence" / "index.json",
            )
            if path.is_file()
        ]
    matches: list[dict[str, Any]] = []
    index_issues: list[str] = []
    for index_path in index_paths:
        try:
            index = _load_json(index_path)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            index_issues.append(f"{index_path}: {exc}")
            continue
        schema = index.get("schema_version")
        if schema == "visual-evidence-index.v1":
            items = _video_frames(root, index_path, index)
        elif schema == "course-material-visual-index.v1":
            items = _course_images(root, index_path, index)
        else:
            index_issues.append(f"{index_path}: unsupported schema {schema!r}")
            continue
        for item in items:
            if not _matches(
                item,
                claim_id=claim_id,
                video_id=video_id,
                request_id=request_id,
                asset_id=asset_id,
                page=page,
                timestamp=timestamp,
                tolerance=tolerance,
            ):
                continue
            checked = dict(item)
            checked["integrity"] = _integrity(root, item)
            matches.append(checked)
    missing_integrity = sum(item["integrity"].get("integrity") != "PASS" for item in matches)
    if not matches:
        status = "NO_MATCH"
    elif index_issues or missing_integrity:
        status = "REVIEW_REQUIRED"
    else:
        status = "PASS"
    return {
        "schema_version": SCHEMA_VERSION,
        "tool_version": TOOL_VERSION,
        "status": status,
        "root": str(root),
        "index_paths": [str(path) for path in index_paths],
        "filters": {
            "claim_id": claim_id,
            "video_id": video_id,
            "request_id": request_id,
            "asset_id": asset_id,
            "page": page,
            "timestamp_seconds": timestamp,
            "timestamp_tolerance": tolerance,
        },
        "match_count": len(matches),
        "integrity_failures": missing_integrity,
        "index_issues": index_issues,
        "matches": matches,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--index", action="append", type=Path, help="index JSON; repeatable")
    parser.add_argument("--claim-id")
    parser.add_argument("--video-id")
    parser.add_argument("--request-id")
    parser.add_argument("--asset-id")
    parser.add_argument("--page", type=int)
    parser.add_argument("--timestamp", type=float)
    parser.add_argument("--tolerance", type=float, default=2.0)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    payload = lookup(
        args.root,
        indexes=args.index,
        claim_id=args.claim_id,
        video_id=args.video_id,
        request_id=args.request_id,
        asset_id=args.asset_id,
        page=args.page,
        timestamp=args.timestamp,
        tolerance=args.tolerance,
    )
    encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = args.output if args.output.is_absolute() else Path(args.root) / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary = output.with_name(f".{output.name}.tmp")
        temporary.write_text(encoded, encoding="utf-8")
        temporary.replace(output)
    if args.json or args.output is None:
        print(encoded, end="")
    return 0 if payload["status"] == "PASS" else (1 if payload["status"] == "REVIEW_REQUIRED" else 2)


if __name__ == "__main__":
    raise SystemExit(main())
