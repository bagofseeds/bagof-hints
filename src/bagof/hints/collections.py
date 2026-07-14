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

from ._internal.typevars.co import K as K_co
from ._internal.typevars.co import T as T_co


@tx.runtime_checkable
class Container(tx.Protocol[T_co]):
    """See [`collections.abc.Container`][]."""

    def __contains__(self, value: T_co) -> bool: ...


@tx.runtime_checkable
class Hashable(tx.Protocol):
    """See [`collections.abc.Hashable`][]."""

    def __hash__(self) -> int: ...


@tx.runtime_checkable
class Iterable(tx.Protocol[T_co]):
    """See [`collections.abc.Iterable`][]."""

    def __iter__(self) -> tx.Iterable[T_co]: ...


@tx.runtime_checkable
class Iterator(Iterable[T_co], tx.Protocol[T_co]):
    """See [`collections.abc.Iterator`][]."""

    def __next__(self) -> T_co: ...


@tx.runtime_checkable
class Reversible(Iterable[T_co], tx.Protocol[T_co]):
    """See [`collections.abc.Reversible`][]."""

    def __reversed__(self) -> None: ...


YieldType = tx.TypeVar("YieldType", covariant=True, default=tx.Any)
SendType = tx.TypeVar("SendType", contravariant=True, default=None)
ReturnType = tx.TypeVar("ReturnType", covariant=True, default=None)


@tx.runtime_checkable
class Generator(
  Iterator[YieldType],
  tx.Protocol[YieldType, SendType, ReturnType]
):
    """See [`collections.abc.Generator`][]."""

    def send(self, value: SendType) -> YieldType: ...

    def throw(self, value: ReturnType) -> YieldType: ...

    def close(self) -> tx.Optional[ReturnType]: ...


@tx.runtime_checkable
class Sized(tx.Protocol[T_co]):
    """See [`collections.abc.Sized`][]."""

    def __len__(self) -> int: ...


@tx.runtime_checkable
class Collection(
    Sized[T_co],
    Iterable[T_co],
    Container[T_co],
    tx.Protocol[T_co]
):
    """See [`collections.abc.Collection`][]."""

    ...


@tx.runtime_checkable
class Sequence(
    Reversible[T_co],
    Collection[T_co],
    tx.Protocol[T_co]
):
    """See [`collections.abc.Sequence`][]."""

    def index(self, value: T_co) -> int: ...

    def count(self, value: T_co) -> int: ...

    def __getitem__(self, index: int) -> T_co: ...


@tx.runtime_checkable
class MutableSequence(Sequence[T_co], tx.Protocol[T_co]):
    """
    See [`collections.abc.MutableSequence`][].
    """

    def __setitem__(self, index: int, value: T_co) -> None: ...

    def __delitem__(self, index: int) -> None: ...

    def insert(self, index: int, value: T_co) -> None: ...

    def append(self, value: T_co) -> None: ...

    def extend(self, values: Iterable[T_co]) -> None: ...

    def reverse(self) -> None: ...

    def clear(self) -> None: ...

    def remove(self, value: T_co) -> None: ...

    def pop(self, index: int = ...) -> T_co: ...

    def __iadd__(self, other: Iterable[T_co]) -> None: ...


@tx.runtime_checkable
class Set(Collection[K_co], tx.Protocol[K_co]):
    """See [`collections.abc.Set`][]."""

    def __le__(self, other: tx.Self) -> bool: ...

    def __lt__(self, other: tx.Self) -> bool: ...

    def __eq__(self, other: tx.Self) -> bool: ...

    def __ne__(self, other: tx.Self) -> bool: ...

    def __gt__(self, other: tx.Self) -> bool: ...

    def __ge__(self, other: tx.Self) -> bool: ...

    def __and__(self, other: tx.Self) -> tx.Self: ...

    def __or__(self, other: tx.Self) -> tx.Self: ...

    def __sub__(self, other: tx.Self) -> tx.Self: ...

    def __rsub__(self, other: tx.Self) -> tx.Self: ...

    def __xor__(self, other: tx.Self) -> tx.Self: ...

    def __rxor__(self, other: tx.Self) -> tx.Self: ...

    def isdisjoint(self, other: Iterable[K_co]) -> bool: ...


@tx.runtime_checkable
class MutableSet(Set[K_co], tx.Protocol[K_co]):
    """See [`collections.abc.MutableSet`][]."""

    def add(self, value: K_co) -> None: ...

    def discard(self, value: K_co) -> None: ...

    def clear(self) -> None: ...

    def pop(self) -> K_co: ...

    def remove(self, value: K_co) -> None: ...

    def __iand__(self, other: tx.Self) -> tx.Self: ...

    def __ior__(self, other: tx.Self) -> tx.Self: ...

    def __isub__(self, other: tx.Self) -> tx.Self: ...

    def __ixor__(self, other: tx.Self) -> tx.Self: ...


ItemType: tx.TypeAlias = tx.Tuple[K_co, T_co]


@tx.runtime_checkable
class Mapping(Collection[K_co], tx.Protocol[K_co, T_co]):
    """See [`collections.abc.Mapping`][]."""

    def __getitem__(self, key: K_co) -> T_co: ...

    def keys(self) -> Iterable[K_co]: ...

    def values(self) -> Iterable[T_co]: ...

    def items(self) -> Iterable[ItemType]: ...

    def get(self, key: K_co, default: T_co = ...) -> T_co: ...

    def __eq__(self, other: tx.Self) -> bool: ...

    def __ne__(self, other: tx.Self) -> bool: ...


@tx.runtime_checkable
class MutableMapping(Mapping[K_co, T_co], tx.Protocol[T_co]):
    """
    See [`collections.abc.MutableMapping`][].
    """

    def __setitem__(self, key: K_co, value: T_co) -> None: ...

    def __delitem__(self, key: K_co) -> None: ...

    def pop(self, key: K_co, default: T_co = ...) -> T_co: ...

    def popitem(self) -> ItemType: ...

    def clear(self) -> None: ...

    def update(self, other: Mapping[K_co, T_co]) -> None: ...

    def setdefault(self, key: K_co, value: T_co) -> None: ...


@tx.runtime_checkable
class Awaitable(tx.Protocol[T_co]):
    """See [`collections.abc.Awaitable`][]."""

    def __await__(self) -> tx.Iterator[T_co]: ...


@tx.runtime_checkable
class Buffer(tx.Protocol[T_co]):
    """See [`collections.abc.Buffer`][]."""

    def __buffer__(self, flags: int) -> memoryview: ...
