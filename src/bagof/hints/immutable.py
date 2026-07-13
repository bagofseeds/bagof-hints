"""
Immutable collections.

The stdlib hints or abc that are not marked as "Mutable" (such as
[collections.abc.MutableSequence][]), represent objects that may or
may not be mutable. The type hints in this module represent
collections that are _specifically_ immutables
"""
__all__ = ["ImmutableSequence", "ImmutableSet", "ImmutableMapping"]

import typing_extensions as tx

from .collections import Iterable, Mapping, Sequence, Set
from .typevars.co import K as K_co
from .typevars.co import T as T_co


@tx.runtime_checkable
class ImmutableSequence(Sequence[T_co], tx.Protocol[T_co]):
    """An immutable [collections.abc.Sequence][]."""

    __setitem__ = tx.NotRequired[tx.Callable[[int, T_co], tx.Never]]
    __delitem__ = tx.NotRequired[tx.Callable[[int], tx.Never]]
    insert = tx.NotRequired[tx.Callable[[int, T_co], tx.Never]]
    append = tx.NotRequired[tx.Callable[[T_co], tx.Never]]
    extend = tx.NotRequired[tx.Callable[[Iterable[T_co]], tx.Never]]
    reverse = tx.NotRequired[tx.Callable[[], tx.Never]]
    clear = tx.NotRequired[tx.Callable[[], tx.Never]]
    remove = tx.NotRequired[tx.Callable[[T_co], tx.Never]]
    pop = tx.NotRequired[tx.Callable[[int], tx.Never]]
    __iadd__ = tx.NotRequired[tx.Callable[[Iterable[T_co]], tx.Never]]


@tx.runtime_checkable
class ImmutableSet(Set[K_co], tx.Protocol[K_co]):
    """An immutable [collections.abc.Set][]."""

    add = tx.NotRequired[tx.Callable[[K_co], tx.Never]]
    discard = tx.NotRequired[tx.Callable[[K_co], tx.Never]]
    clear = tx.NotRequired[tx.Callable[[], tx.Never]]
    pop = tx.NotRequired[tx.Callable[[], tx.Never]]
    remove = tx.NotRequired[tx.Callable[[K_co], tx.Never]]
    __iand__ = tx.NotRequired[tx.Callable[[Set[K_co]], tx.Never]]
    __ior__ = tx.NotRequired[tx.Callable[[Set[K_co]], tx.Never]]
    __isub__ = tx.NotRequired[tx.Callable[[Set[K_co]], tx.Never]]
    __ixor__ = tx.NotRequired[tx.Callable[[Set[K_co]], tx.Never]]


@tx.runtime_checkable
class ImmutableMapping(Mapping[K_co, T_co], tx.Protocol[K_co, T_co]):
    """An immutable [collections.abc.Mapping][]."""

    __setitem__ = tx.NotRequired[tx.Callable[[K_co, T_co], tx.Never]]
    __delitem__ = tx.NotRequired[tx.Callable[[K_co], tx.Never]]
    pop = tx.NotRequired[tx.Callable[[K_co, T_co], tx.Never]]
    popitem = tx.NotRequired[tx.Callable[[K_co], tx.Never]]
    clear = tx.NotRequired[tx.Callable[[], tx.Never]]
    update = tx.NotRequired[tx.Callable[[Mapping[K_co, T_co]], tx.Never]]
    setdefault = tx.NotRequired[tx.Callable[[K_co, T_co], tx.Never]]
