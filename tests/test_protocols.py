"""Runtime structural conformance tests for the exported protocols.

The [`collections`][bagof.hints.collections] protocols are decorated with
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
    # ``Sequence`` does not require ``__reversed__``, so builtins that lack it
    # (tuple, str, range) conform -- matching the members abc.Sequence
    # registers, even though they only reverse via the len/getitem fallback.
    (Sequence, (1, 2), True),
    (Sequence, "ab", True),
    (Sequence, range(3), True),
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
    # ``Reversible`` *does* require ``__reversed__``: a list has it, a plain
    # tuple does not (it reverses via the len/getitem fallback instead).
    (Reversible, [1, 2], True),
    (Reversible, (1, 2), False),
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
