"""Tests that validate `mypy` support for the exported hints."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
import typing_extensions as tx


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


VALID = [  # (VAR, HINT, VALUE, [IMPORT])
    ('JSON', '{"items": [1, "two", False, None]}',
     'from bagof.hints import JSON'),
    ('JSONDict', '{"items": [1, "two"]}',
     'from bagof.hints import JSONDict'),
    ('MutableJSONDict', '{"items": [1, "two"]}',
     'from bagof.hints import MutableJSONDict'),
    ('PathLike', 'Path("demo.txt")',
     'from pathlib import Path', 'from bagof.hints import PathLike'),
    ('StringLike', 'memoryview(b"abc")',
     'from bagof.hints import StringLike'),
    ('OneOrIter[int]', '(1, 2, 3)',
     'from bagof.hints import OneOrIter'),
    ('OneOrSeq[int]', '[1, 2, 3]',
     'from bagof.hints import OneOrSeq'),
    ('BuiltinSequence[int]', '(1, 2, 3)',
     'from bagof.hints import BuiltinSequence'),
]

INVALID = [
    ('JSON', '{1: "value"}',
     'from bagof.hints import JSON'),
    ('JSONDict', '{"ok": {1: "value"}}',
     'from bagof.hints import JSONDict'),
    ('PathLike', '3',
     'from bagof.hints import PathLike'),
    ('BuiltinSequence[int]', '{1, 2}',
     'from bagof.hints import BuiltinSequence'),
]


@pytest.mark.parametrize("line", VALID)
def test_mypy_valid(tmp_path: Path, line: tx.Iterable[str]) -> None:
    """Mypy should accept valid uses of the exported hints."""
    path = tmp_path / "valid_hints.py"
    hint, value, *imports = line
    statement = f"x: {hint} = {value}"
    text = "\n".join([*imports, statement])
    print(text)
    path.write_text(text, encoding="utf-8")

    result = run_mypy(path)

    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("line", INVALID)
def test_mypy_invalid(tmp_path: Path, line: tx.Iterable[str]) -> None:
    """Mypy should reject incompatible values for the exported hints."""
    path = tmp_path / "invalid_hints.py"
    hint, value, *imports = line
    statement = f"x: {hint} = {value}"
    text = "\n".join([*imports, statement])
    print(text)
    path.write_text(text, encoding="utf-8")

    result = run_mypy(path)
    output = result.stdout + result.stderr

    assert result.returncode != 0, output
    # Each parametrized case checks a single statement, so mypy reports a
    # single error. (The previous ``>= 4`` threshold assumed all INVALID
    # cases were type-checked in one file.)
    assert output.count(": error:") >= 1, output
