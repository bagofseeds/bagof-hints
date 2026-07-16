"""Tests that validate `mypy` support for the exported hints."""

from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path

import pytest
import typing_extensions as tx

# numpy ships stubs that use ``type X = ...`` (PEP 695), which mypy rejects
# under ``--python-version 3.8``. The tests only care about ``bagof.hints``'
# own types, so we tell mypy to skip analysing numpy's stubs.
_MYPY_CONFIG = (
    "[mypy]\n\n"
    "[mypy-numpy.*]\n"
    "follow_imports = skip\n"
    "follow_imports_for_stubs = true\n"
)


def run_mypy(path: Path) -> subprocess.CompletedProcess[str]:
    """Run mypy on a test file."""
    config = path.parent / "mypy.ini"
    config.write_text(_MYPY_CONFIG, encoding="utf-8")
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--strict",
            "--python-version",
            "3.8",
            "--config-file",
            str(config),
            str(path),
        ],
        capture_output=True,
        check=False,
        cwd=path.parent,
        text=True,
    )


VALID = [  # (HINT, VALUE, *IMPORTS)
    # -- builtin scalars ----------------------------------------------------
    ('BuiltinIntegral', '3',
     'from bagof.hints import BuiltinIntegral'),
    ('BuiltinReal', '3',
     'from bagof.hints import BuiltinReal'),
    ('BuiltinReal', '3.5',
     'from bagof.hints import BuiltinReal'),
    ('BuiltinNumber', '1j',
     'from bagof.hints import BuiltinNumber'),
    ('BuiltinScalar', '"text"',
     'from bagof.hints import BuiltinScalar'),
    ('BuiltinSequence[int]', '(1, 2, 3)',
     'from bagof.hints import BuiltinSequence'),
    ('BuiltinSequence[int]', '[1, 2, 3]',
     'from bagof.hints import BuiltinSequence'),
    # -- json ---------------------------------------------------------------
    ('JSONNumber', '3.5',
     'from bagof.hints import JSONNumber'),
    ('JSONScalar', 'None',
     'from bagof.hints import JSONScalar'),
    ('JSONScalar', 'True',
     'from bagof.hints import JSONScalar'),
    ('JSON', '{"items": [1, "two", False, None]}',
     'from bagof.hints import JSON'),
    ('JSON', '{"a": {"b": [1, 2.0, "x", None]}}',
     'from bagof.hints import JSON'),
    ('JSONDict', '{"items": [1, "two"]}',
     'from bagof.hints import JSONDict'),
    ('MutableJSON', '[1, "two", None]',
     'from bagof.hints import MutableJSON'),
    ('MutableJSONDict', '{"items": [1, "two"]}',
     'from bagof.hints import MutableJSONDict'),
    # -- strings ------------------------------------------------------------
    ('BytesLike', 'b"abc"',
     'from bagof.hints import BytesLike'),
    ('BytesLike', 'bytearray(b"abc")',
     'from bagof.hints import BytesLike'),
    ('StringLike', '"abc"',
     'from bagof.hints import StringLike'),
    ('StringLike', 'memoryview(b"abc")',
     'from bagof.hints import StringLike'),
    ('PathLike', '"demo.txt"',
     'from bagof.hints import PathLike'),
    ('PathLike', 'Path("demo.txt")',
     'from pathlib import Path', 'from bagof.hints import PathLike'),
    # -- flexi --------------------------------------------------------------
    ('OneOrIter[int]', '3',
     'from bagof.hints import OneOrIter'),
    ('OneOrIter[int]', '(1, 2, 3)',
     'from bagof.hints import OneOrIter'),
    ('OneOrSeq[int]', '3',
     'from bagof.hints import OneOrSeq'),
    ('OneOrSeq[int]', '[1, 2, 3]',
     'from bagof.hints import OneOrSeq'),
    # -- unpackable ---------------------------------------------------------
    ('Unpackable[int]', '{"a": 1}',
     'from bagof.hints import Unpackable'),
]

INVALID = [  # (HINT, VALUE, *IMPORTS)
    # -- builtin scalars ----------------------------------------------------
    ('BuiltinIntegral', '"a"',
     'from bagof.hints import BuiltinIntegral'),
    ('BuiltinReal', '"a"',
     'from bagof.hints import BuiltinReal'),
    ('BuiltinNumber', '"a"',
     'from bagof.hints import BuiltinNumber'),
    ('BuiltinScalar', '[1]',
     'from bagof.hints import BuiltinScalar'),
    ('BuiltinSequence[int]', '{1, 2}',
     'from bagof.hints import BuiltinSequence'),
    ('BuiltinSequence[int]', '["a"]',
     'from bagof.hints import BuiltinSequence'),
    # -- json ---------------------------------------------------------------
    ('JSONNumber', '"a"',
     'from bagof.hints import JSONNumber'),
    ('JSONScalar', '[1]',
     'from bagof.hints import JSONScalar'),
    ('JSON', '{1: "value"}',
     'from bagof.hints import JSON'),
    ('JSON', '{1, 2}',
     'from bagof.hints import JSON'),
    ('JSONDict', '{"ok": {1: "value"}}',
     'from bagof.hints import JSONDict'),
    ('MutableJSON', '(1, "a")',
     'from bagof.hints import MutableJSON'),
    ('MutableJSONDict', '{1: 1}',
     'from bagof.hints import MutableJSONDict'),
    # -- strings ------------------------------------------------------------
    ('BytesLike', '"a"',
     'from bagof.hints import BytesLike'),
    ('StringLike', '3',
     'from bagof.hints import StringLike'),
    ('PathLike', '3',
     'from bagof.hints import PathLike'),
    # -- flexi --------------------------------------------------------------
    ('OneOrIter[int]', '"a"',
     'from bagof.hints import OneOrIter'),
    ('OneOrSeq[int]', '3.5',
     'from bagof.hints import OneOrSeq'),
    # -- unpackable ---------------------------------------------------------
    ('Unpackable[int]', '[1]',
     'from bagof.hints import Unpackable'),
]


def _make_ids(cases: tx.Iterable[tx.Sequence[str]]) -> tx.List[str]:
    """Build readable parametrization ids from ``(hint, value, ...)`` cases."""
    return [f"{hint} = {value}" for hint, value, *_ in cases]


@pytest.mark.parametrize("line", VALID, ids=_make_ids(VALID))
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


@pytest.mark.parametrize("line", INVALID, ids=_make_ids(INVALID))
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
    # single error. (The threshold used to be ``>= 4``, which assumed all
    # INVALID cases were type-checked together in one file.)
    assert output.count(": error:") >= 1, output


TYPEVAR_BOUND_SNIPPET = textwrap.dedent(
    """
    from bagof.hints.typevars.inv import INT


    def identity(value: INT) -> INT:
        return value


    identity(3)         # ok: int
    identity(True)      # ok: bool is a subtype of int
    identity("nope")    # error: str violates ``bound=int``
    """
)


def test_mypy_typevar_bound(tmp_path: Path) -> None:
    """A bounded ``TypeVar`` should reject arguments outside its bound."""
    path = tmp_path / "typevar_bound.py"
    path.write_text(TYPEVAR_BOUND_SNIPPET, encoding="utf-8")

    result = run_mypy(path)
    output = result.stdout + result.stderr

    assert result.returncode != 0, output
    # Only the ``str`` call violates the ``bound=int`` constraint.
    assert output.count(": error:") == 1, output
    assert "[type-var]" in output, output
