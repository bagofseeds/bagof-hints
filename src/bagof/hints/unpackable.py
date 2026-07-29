"""Objects unpackable into keyword arguments."""
__all__ = ["Unpackable"]

import typing_extensions as tx

from ._internal.typevars.co import T as T_co


class Unpackable(tx.Protocol[T_co]):
    """
    A protocol for objects that can be unpacked using the `**` syntax.

    Unpacking a mapping-like object into keyword arguments only requires
    `keys()` and `__getitem__`, so this protocol is deliberately narrower
    than [`Mapping`][bagof.hints.collections.Mapping]. The parameter is the
    *value* type; keys are always strings, since they become keyword
    argument names.
    """

    def keys(self) -> tx.Iterable[str]: ...

    def __getitem__(self, key: str) -> T_co: ...
