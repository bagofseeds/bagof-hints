"""Protocols that are compatible with [`collections.abc`][]"""
__all__ = [
    "Container",
    "Hashable",
    "Iterable",
    "Iterator",
    "Reversible",
    "Generator",
    "Sized",
    "Collection",
    "Sequence",
    "MutableSequence",
    "Set",
    "MutableSet",
    "Mapping",
    "MutableMapping",
    "Awaitable",
    "Buffer",
]
# Import stdlib so that mkdocstring correctly resolves cross-references
import collections.abc  # noqa: F401

import typing_extensions as tx

# Covariant TypeVars are used for read-only ("producer") positions, invariant
# ones for read/write ("consumer") positions. This mirrors the variance rules
# used by the standard library (e.g. ``Sequence`` is covariant while
# ``MutableSequence`` is invariant, and a ``Mapping``'s key type is invariant).
from ._internal.typevars.co import K as K_co
from ._internal.typevars.co import T as T_co
from ._internal.typevars.inv import K as K_inv
from ._internal.typevars.inv import T as T_inv


@tx.runtime_checkable
class Container(tx.Protocol[T_co]):
    """See [`collections.abc.Container`][]."""

    def __contains__(self, value: object) -> bool: ...


@tx.runtime_checkable
class Hashable(tx.Protocol):
    """See [`collections.abc.Hashable`][]."""

    def __hash__(self) -> int: ...


@tx.runtime_checkable
class Iterable(tx.Protocol[T_co]):
    """See [`collections.abc.Iterable`][]."""

    def __iter__(self) -> "Iterator[T_co]": ...


@tx.runtime_checkable
class Iterator(Iterable[T_co], tx.Protocol[T_co]):
    """See [`collections.abc.Iterator`][]."""

    def __next__(self) -> T_co: ...

    def __iter__(self) -> "Iterator[T_co]": ...


@tx.runtime_checkable
class Reversible(Iterable[T_co], tx.Protocol[T_co]):
    """See [`collections.abc.Reversible`][].

    This is a purely *structural* check for a ``__reversed__`` method.
    Builtins that are reversible only through the ``__len__``/``__getitem__``
    fallback used by [`reversed`][] (``tuple``, ``str``, ``bytes``,
    ``range``, ...) do **not** expose ``__reversed__``, so they are *not*
    instances of this protocol -- unlike `collections.abc.Reversible`, which
    reports them as virtual subclasses via registration rather than structure.
    """

    def __reversed__(self) -> Iterator[T_co]: ...


YieldType = tx.TypeVar("YieldType", covariant=True, default=tx.Any)
SendType = tx.TypeVar("SendType", contravariant=True, default=None)
ReturnType = tx.TypeVar("ReturnType", covariant=True, default=None)


@tx.runtime_checkable
class Generator(
    Iterator[YieldType],
    tx.Protocol[YieldType, SendType, ReturnType],
):
    """See [`collections.abc.Generator`][]."""

    def send(self, value: SendType) -> YieldType: ...

    def throw(self, value: BaseException) -> YieldType: ...

    def close(self) -> tx.Optional[ReturnType]: ...


@tx.runtime_checkable
class Sized(tx.Protocol):
    """See [`collections.abc.Sized`][]."""

    def __len__(self) -> int: ...


@tx.runtime_checkable
class Collection(
    Sized,
    Iterable[T_co],
    Container[T_co],
    tx.Protocol[T_co],
):
    """See [`collections.abc.Collection`][]."""

    ...


@tx.runtime_checkable
class Sequence(
    Collection[T_co],
    tx.Protocol[T_co],
):
    """A read-only sequence, structurally close to
    [`collections.abc.Sequence`][].

    !!! note
        Unlike the standard library's ABC, this protocol does **not**
        derive from [`Reversible`][bagof.hints.collections.Reversible]
        and so does not require a ``__reversed__`` method. This is
        deliberate: ``tuple``, ``str``, ``bytes`` and ``range`` are
        reversible only through the ``__len__``/``__getitem__`` fallback
        used by [`reversed`][] and do not expose ``__reversed__``
        themselves. Requiring it would make those builtins fail a
        structural ``isinstance`` check, even though
        `collections.abc.Sequence` -- which relies on explicit
        registration rather than structure -- treats them as sequences.
        Use [`Reversible`][bagof.hints.collections.Reversible]
        explicitly when a ``__reversed__`` method is actually required.
    """

    def __getitem__(self, index: int) -> T_co: ...

    def index(self, value: object, start: int = ..., stop: int = ...) -> int:
        ...

    def count(self, value: object) -> int: ...


@tx.runtime_checkable
class MutableSequence(Sequence[T_inv], tx.Protocol[T_inv]):
    """See [`collections.abc.MutableSequence`][]."""

    def __setitem__(self, index: int, value: T_inv) -> None: ...

    def __delitem__(self, index: int) -> None: ...

    def insert(self, index: int, value: T_inv) -> None: ...

    def append(self, value: T_inv) -> None: ...

    def extend(self, values: Iterable[T_inv]) -> None: ...

    def reverse(self) -> None: ...

    def clear(self) -> None: ...

    def remove(self, value: T_inv) -> None: ...

    def pop(self, index: int = ...) -> T_inv: ...

    def __iadd__(self, values: Iterable[T_inv]) -> "MutableSequence[T_inv]":
        ...


@tx.runtime_checkable
class Set(Collection[K_co], tx.Protocol[K_co]):
    """See [`collections.abc.Set`][]."""

    def __le__(self, other: "Set[object]") -> bool: ...

    def __lt__(self, other: "Set[object]") -> bool: ...

    def __gt__(self, other: "Set[object]") -> bool: ...

    def __ge__(self, other: "Set[object]") -> bool: ...

    def __and__(self, other: "Set[object]") -> "Set[K_co]": ...

    def __or__(self, other: "Set[object]") -> "Set[K_co]": ...

    def __sub__(self, other: "Set[object]") -> "Set[K_co]": ...

    def __xor__(self, other: "Set[object]") -> "Set[K_co]": ...

    def isdisjoint(self, other: Iterable[object]) -> bool: ...


@tx.runtime_checkable
class MutableSet(Set[K_inv], tx.Protocol[K_inv]):
    """See [`collections.abc.MutableSet`][]."""

    def add(self, value: K_inv) -> None: ...

    def discard(self, value: K_inv) -> None: ...

    def clear(self) -> None: ...

    def pop(self) -> K_inv: ...

    def remove(self, value: K_inv) -> None: ...

    def __ior__(self, other: "Set[object]") -> "MutableSet[K_inv]": ...

    def __iand__(self, other: "Set[object]") -> "MutableSet[K_inv]": ...

    def __isub__(self, other: "Set[object]") -> "MutableSet[K_inv]": ...

    def __ixor__(self, other: "Set[object]") -> "MutableSet[K_inv]": ...


@tx.runtime_checkable
class Mapping(Collection[K_inv], tx.Protocol[K_inv, T_co]):
    """See [`collections.abc.Mapping`][].

    The key type is invariant and the value type is covariant, matching the
    standard library's ``Mapping``.
    """

    def __getitem__(self, key: K_inv) -> T_co: ...

    def keys(self) -> Iterable[K_inv]: ...

    def values(self) -> Iterable[T_co]: ...

    def items(self) -> Iterable[tx.Tuple[K_inv, T_co]]: ...

    def get(self, key: K_inv, default: object = ...) -> tx.Optional[T_co]: ...


@tx.runtime_checkable
class MutableMapping(Mapping[K_inv, T_inv], tx.Protocol[K_inv, T_inv]):
    """See [`collections.abc.MutableMapping`][]."""

    def __setitem__(self, key: K_inv, value: T_inv) -> None: ...

    def __delitem__(self, key: K_inv) -> None: ...

    def pop(self, key: K_inv, default: T_inv = ...) -> T_inv: ...

    def popitem(self) -> tx.Tuple[K_inv, T_inv]: ...

    def clear(self) -> None: ...

    def update(self, other: Mapping[K_inv, T_inv]) -> None: ...

    def setdefault(self, key: K_inv, default: T_inv = ...) -> T_inv: ...


@tx.runtime_checkable
class Awaitable(tx.Protocol[T_co]):
    """See [`collections.abc.Awaitable`][]."""

    def __await__(self) -> tx.Iterator[T_co]: ...


@tx.runtime_checkable
class Buffer(tx.Protocol):
    """See [`collections.abc.Buffer`][]."""

    def __buffer__(self, flags: int) -> memoryview: ...
