"""Coverage for the reusable ``TypeVar`` collections.

The four modules under [`bagof.hints.typevars`][] expose the *same* set of
names, each declared with a different variance:

| module   | variance        |
| -------- | --------------- |
| `co`     | covariant       |
| `contra` | contravariant   |
| `infer`  | inferred        |
| `inv`    | invariant       |
"""

from __future__ import annotations

import numbers

import pytest
import typing_extensions as tx

from bagof.hints.typevars import co, contra, infer, inv

MODULES = {
    "co": (co, "covariant"),
    "contra": (contra, "contravariant"),
    "infer": (infer, "infer"),
    "inv": (inv, "invariant"),
}

# Expected ``__bound__`` for the scalar / numeric TypeVars. ``T`` is unbound;
# ``K`` is hashable; every other name is expected to carry *some* bound.
EXPECTED_BOUNDS = {
    "STR": str,
    "BYTES": bytes,
    "BOOL": bool,
    "INT": int,
    "FLOAT": float,
    "COMPLEX": complex,
    "INTEGRAL": numbers.Integral,
    "REAL": numbers.Real,
    "NUMBER": numbers.Number,
    "K": tx.Hashable,
}


def _variance(tv: tx.TypeVar) -> str:
    """Return the variance of a ``TypeVar`` as a string."""
    if getattr(tv, "__infer_variance__", False):
        return "infer"
    if tv.__covariant__:
        return "covariant"
    if tv.__contravariant__:
        return "contravariant"
    return "invariant"


def _all_typevars() -> tx.List[tx.Tuple[str, object, str, str]]:
    """Yield ``(key, module, variance, name)`` for every exported TypeVar."""
    cases = []
    for key, (mod, variance) in MODULES.items():
        for name in mod.__all__:
            cases.append((key, mod, variance, name))
    return cases


ALL_TYPEVARS = _all_typevars()
ALL_IDS = [f"{key}.{name}" for key, _, _, name in ALL_TYPEVARS]


@pytest.mark.parametrize(
    "key,mod,variance,name", ALL_TYPEVARS, ids=ALL_IDS
)
def test_typevar_is_typevar(
    key: str, mod: object, variance: str, name: str
) -> None:
    """Every name declared in ``__all__`` resolves to a ``TypeVar``."""
    tv = getattr(mod, name)
    assert isinstance(tv, tx.TypeVar), f"{key}.{name} is not a TypeVar"


@pytest.mark.parametrize(
    "key,mod,variance,name", ALL_TYPEVARS, ids=ALL_IDS
)
def test_typevar_bound(
    key: str, mod: object, variance: str, name: str
) -> None:
    """TypeVars carry the expected ``__bound__``."""
    tv = getattr(mod, name)
    if name in EXPECTED_BOUNDS:
        assert tv.__bound__ is EXPECTED_BOUNDS[name]
    elif name == "T":
        # ``T`` is the generic default TypeVar and is intentionally unbound.
        assert tv.__bound__ is None
    else:
        assert tv.__bound__ is not None, f"{key}.{name} should be bounded"


@pytest.mark.parametrize(
    "key,mod,variance,name", ALL_TYPEVARS, ids=ALL_IDS
)
def test_typevar_variance(
    key: str, mod: object, variance: str, name: str
) -> None:
    """TypeVars declare the variance advertised by their module."""
    assert _variance(getattr(mod, name)) == variance


def test_eager_typevars_are_numpy_free() -> None:
    """
    The top-level ``typevars`` modules no longer carry the numpy-bound
    ``DTYPE`` / ``DTYPELIKE`` -- those moved to ``bagof.hints.numpy.typevars``
    so that importing ``bagof.hints`` never imports numpy.
    """
    for mod, _ in MODULES.values():
        assert "DTYPE" not in mod.__all__
        assert "DTYPELIKE" not in mod.__all__
