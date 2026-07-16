"""Runtime structural conformance tests for the exported protocols.

The [`collections`][bagof.hints.collections] and
[`immutable`][bagof.hints.immutable] protocols are decorated with
``@runtime_checkable``, so ``isinstance`` performs a structural
(method-presence) check. These tests pin that behaviour for the concrete
builtins each protocol is meant to describe.
"""

from __future__ import annotations

import pytest
import typing_extensions as tx

import bagof.hints as hints
from bagof.hints import (
    Collection,
    Container,
    Hashable,
    ImmutableMapping,
    ImmutableSequence,
    ImmutableSet,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Reversible,
    Sequence,
    Set,
    Sized,
)

# Protocols that must be usable with ``isinstance``.
RUNTIME_CHECKABLE = [
    "Container", "Hashable", "Iterable", "Iterator", "Reversible", "Sized",
    "Collection", "Sequence", "MutableSequence", "Set", "MutableSet",
    "Mapping", "MutableMapping", "Awaitable", "Buffer",
    "ImmutableSequence", "ImmutableSet", "ImmutableMapping",
]


@pytest.mark.parametrize("name", RUNTIME_CHECKABLE)
def test_is_runtime_checkable_protocol(name: str) -> None:
    """Every exported protocol should be a runtime-checkable ``Protocol``."""
    proto = getattr(hints, name)
    assert tx.is_protocol(proto), f"{name} is not a Protocol"
    assert getattr(proto, "_is_runtime_protocol", False), (
        f"{name} is not @runtime_checkable"
    )


# (protocol, value, is_instance)
CONFORMANCE = [
    (Container, [1, 2], True),
    (Hashable, 3, True),
    (Hashable, [1], False),
    (Iterable, [1], True),
    (Iterable, 3, False),
    (Iterator, iter([1]), True),
    (Iterator, [1], False),
    (Sized, [1], True),
    (Sized, 3, False),
    (Collection, [1], True),
    (Collection, 3, False),
    (Sequence, [1, 2], True),
    # NB: a plain ``tuple`` has no ``__reversed__`` attribute, so it does not
    # satisfy the (structural) ``Reversible``-derived ``Sequence`` protocol.
    (Sequence, 3, False),
    (MutableSequence, [1], True),
    (MutableSequence, (1,), False),
    (Set, {1}, True),
    (Set, [1], False),
    (MutableSet, {1}, True),
    (MutableSet, frozenset({1}), False),
    (Mapping, {"a": 1}, True),
    (Mapping, [1], False),
    (MutableMapping, {"a": 1}, True),
    (MutableMapping, (1,), False),
    (Reversible, [1, 2], True),
]


@pytest.mark.parametrize(
    "protocol,value,expected",
    CONFORMANCE,
    ids=[f"{p.__name__}:{v!r}" for p, v, _ in CONFORMANCE],
)
def test_runtime_conformance(
    protocol: type, value: object, expected: bool
) -> None:
    """Concrete builtins conform (or not) to the collections protocols."""
    assert isinstance(value, protocol) is expected


# ---------------------------------------------------------------------------
# Immutable protocols
#
# These protocols describe *specifically immutable* collections (see
# ``immutable.py``). Structural typing cannot assert the *absence* of a
# mutating method, so a mutable ``list`` may still satisfy
# ``ImmutableSequence`` structurally. The cases below encode the *intended*
# semantics and are marked ``xfail`` where structural typing cannot honour
# them.
# ---------------------------------------------------------------------------
IMMUTABLE_INTENDED = [
    pytest.param(ImmutableSequence, (1, 2), True, id="tuple-is-immutable-seq"),
    pytest.param(
        ImmutableSequence, [1, 2], False, id="list-is-not-immutable-seq",
        marks=pytest.mark.xfail(
            reason="structural protocols cannot reject a mutable list",
            strict=False,
        ),
    ),
    pytest.param(
        ImmutableSet, frozenset({1}), True, id="frozenset-is-immutable-set",
    ),
    pytest.param(
        ImmutableSet, {1}, False, id="set-is-not-immutable-set",
        marks=pytest.mark.xfail(
            reason="structural protocols cannot reject a mutable set",
            strict=False,
        ),
    ),
    pytest.param(
        ImmutableMapping, {"a": 1}, False, id="dict-is-not-immutable-mapping",
        marks=pytest.mark.xfail(
            reason="structural protocols cannot reject a mutable dict",
            strict=False,
        ),
    ),
]


@pytest.mark.parametrize("protocol,value,expected", IMMUTABLE_INTENDED)
def test_immutable_intended_semantics(
    protocol: type, value: object, expected: bool
) -> None:
    """Document the *intended* immutability semantics (see the module)."""
    assert isinstance(value, protocol) is expected
