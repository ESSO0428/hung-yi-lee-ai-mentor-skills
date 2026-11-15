#!/usr/bin/env python3
"""Route official course-material search without hiding the package boundary.

The canonical implementation lives in the full Distilly-SKILL repository.  A
copied mentor collection still has a stable command path, but it must report a
missing host source index instead of silently searching an unrelated directory.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys


_USAGE = "usage: search_course_material_chunks.py QUERY [--index PATH] [--text-report PATH] [--root PATH]"


def _find_host_tool() -> Path | None:
    current = Path(__file__).resolve()
    for ancestor in (current.parent, *current.parents):
        candidate = ancestor / "tools" / "search_course_material_chunks.py"
        if candidate == current:
            continue
        if candidate.is_file():
            return candidate
    return None


def main() -> int:
    if any(argument in {"--help", "-h"} for argument in sys.argv[1:]):
        print(_USAGE)
        print("Searches the verified official course-material index when hosted by Distilly-SKILL.")
        return 0
    host_tool = _find_host_tool()
    if host_tool is None:
        payload = {
            "schema_version": "course-material-search.v1",
            "status": "INPUT_MISSING",
            "required_host_capability": "official course-material source index",
            "message": (
                "This mentor copy has no verified official course-material index. "
                "Run it inside Distilly-SKILL or provide a host implementation "
                "that can verify the index and paired text report."
            ),
        }
        sys.stdout.buffer.write((json.dumps(payload, ensure_ascii=False) + "\n").encode("utf-8"))
        return 2

    arguments = list(sys.argv[1:])
    has_root = any(argument == "--root" or argument.startswith("--root=") for argument in arguments)
    if not has_root:
        # The canonical tool resolves relative data/ paths from the repository
        # root, not from this nested collection directory.
        arguments.extend(["--root", str(host_tool.parents[1])])
    return subprocess.run([sys.executable, str(host_tool), *arguments], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
