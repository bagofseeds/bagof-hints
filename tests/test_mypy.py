"""Tests that validate `mypy` support for the exported hints."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path


def run_mypy(path: Path) -> subprocess.CompletedProcess[str]:
    """Run mypy on a test file."""
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--strict",
            "--python-version",
            "3.8",
            str(path),
        ],
        capture_output=True,
        check=False,
        cwd=path.parent,
        text=True,
    )


def test_mypy_accepts_exported_hints(tmp_path: Path) -> None:
    """Mypy should accept valid uses of the exported hints."""
    path = tmp_path / "valid_hints.py"
    path.write_text(
        textwrap.dedent(
            """
            from pathlib import Path

            from bagof.hints import (
                BuiltinSequence,
                JSON,
                JSONDict,
                MutableJSONDict,
                OneOrIter,
                OneOrSeq,
                PathLike,
                StringLike,
            )

            json_value: JSON = {"items": [1, "two", False, None]}
            json_dict: JSONDict = {"items": [1, "two"]}
            mutable_json: MutableJSONDict = {"items": [1, "two"]}
            path_value: PathLike = Path("demo.txt")
            string_value: StringLike = memoryview(b"abc")
            one_or_iter: OneOrIter[int] = (1, 2, 3)
            one_or_seq: OneOrSeq[int] = [1, 2, 3]
            builtin_seq: BuiltinSequence[int] = (1, 2, 3)
            """
        ),
        encoding="utf-8",
    )

    result = run_mypy(path)

    assert result.returncode == 0, result.stdout + result.stderr


def test_mypy_rejects_invalid_values_for_exported_hints(
    tmp_path: Path,
) -> None:
    """Mypy should reject incompatible values for the exported hints."""
    path = tmp_path / "invalid_hints.py"
    path.write_text(
        textwrap.dedent(
            """
            from bagof.hints import BuiltinSequence, JSON, JSONDict, PathLike

            bad_json: JSON = {1: "value"}
            bad_json_dict: JSONDict = {"ok": {1: "value"}}
            bad_path: PathLike = 3
            bad_seq: BuiltinSequence[int] = {1, 2}
            """
        ),
        encoding="utf-8",
    )

    result = run_mypy(path)
    output = result.stdout + result.stderr

    assert result.returncode != 0, output
    assert output.count(": error:") >= 4, output
