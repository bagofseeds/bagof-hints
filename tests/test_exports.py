"""Verify the integrity of the package's public API (``__all__``)."""

from __future__ import annotations

import importlib

import pytest
import typing_extensions as tx

import bagof.hints as hints

# Submodules that re-export their names at the top level via ``*`` imports.
SUBMODULES = [
    "builtin",
    "collections",
    "flexi",
    "immutable",
    "json",
    "strings",
    "unpackable",
]


def _submodule_exports() -> tx.List[tx.Tuple[str, str]]:
    cases = []
    for modname in SUBMODULES:
        mod = importlib.import_module(f"bagof.hints.{modname}")
        for name in mod.__all__:
            cases.append((modname, name))
    return cases


SUBMODULE_EXPORTS = _submodule_exports()


@pytest.mark.parametrize(
    "modname,name",
    SUBMODULE_EXPORTS,
    ids=[f"{m}.{n}" for m, n in SUBMODULE_EXPORTS],
)
def test_submodule_name_reexported(modname: str, name: str) -> None:
    """Each ``<module>.__all__`` name is re-exported at the package root."""
    mod = importlib.import_module(f"bagof.hints.{modname}")
    assert hasattr(mod, name), f"{modname}.{name} declared but missing"
    assert hasattr(hints, name), f"bagof.hints.{name} not re-exported"
    assert getattr(hints, name) is getattr(mod, name), (
        f"bagof.hints.{name} is not the same object as {modname}.{name}"
    )


@pytest.mark.parametrize("name", hints.__all__)
def test_package_all_is_importable(name: str) -> None:
    """Every name in ``bagof.hints.__all__`` is a real attribute."""
    assert hasattr(hints, name), f"bagof.hints.{name} is missing"


def test_package_all_has_no_duplicates() -> None:
    """The aggregated ``__all__`` should not contain duplicate names."""
    duplicates = {
        name for name in hints.__all__ if hints.__all__.count(name) > 1
    }
    assert not duplicates, f"duplicate names in __all__: {sorted(duplicates)}"


def test_version_is_exposed() -> None:
    """The package exposes a ``__version__`` string."""
    assert isinstance(hints.__version__, str)
    assert hints.__version__
