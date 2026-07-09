import typing_extensions as tx

from .collections import Sequence, Mapping, Set, Iterable, T_co, K_co


@tx.runtime_checkable
class ImmutableSequence(Sequence[T_co]):

    __setitem__ = tx.NotRequired[Callable[[int, T_co], Never]]
    __delitem__ = tx.NotRequired[Callable[[int], Never]]
    insert = tx.NotRequired[Callable[[int, T_co], Never]]
    append = tx.NotRequired[Callable[[T_co], Never]]
    extend = tx.NotRequired[Callable[[Iterable[T_co]], Never]]
    reverse = tx.NotRequired[Callable[[], Never]]
    clear = tx.NotRequired[Callable[[], Never]]
    remove = tx.NotRequired[Callable[[T_co], Never]]
    pop = tx.NotRequired[Callable[[int], Never]]
    __iadd__ = tx.NotRequired[Callable[[Iterable[T_co]], Never]]


@tx.runtime_checkable
class ImmutableSet(Set[K_co]):

    add = tx.NotRequired[Callable[[K_co], Never]]
    discard = tx.NotRequired[Callable[[K_co], Never]]
    clear = tx.NotRequired[Callable[[], Never]]
    pop = tx.NotRequired[Callable[[], Never]]
    remove = tx.NotRequired[Callable[[K_co], Never]]
    __iand__ = tx.NotRequired[Callable[[Set[K_co]], Never]]
    __ior__ = tx.NotRequired[Callable[[Set[K_co]], Never]]
    __isub__ = tx.NotRequired[Callable[[Set[K_co]], Never]]
    __ixor__ = tx.NotRequired[Callable[[Set[K_co]], Never]]


@tx.runtime_checkable
class ImmutableMapping(Mapping[K_co, T_co]):

    __setitem__ = tx.NotRequired[Callable[[K_co, T_co], Never]]
    __delitem__ = tx.NotRequired[Callable[[K_co], Never]]
    pop = tx.NotRequired[Callable[[K_co, T_co], Never]]
    popitem = tx.NotRequired[Callable[[K_co], Never]]
    clear = tx.NotRequired[Callable[[], Never]]
    update = tx.NotRequired[Callable[[Mapping[K_co, T_co]], Never]]
    setdefault = tx.NotRequired[Callable[[K_co, T_co], Never]]
