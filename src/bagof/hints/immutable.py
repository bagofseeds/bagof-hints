"""
Immutable collections.

The standard library's hints or abstract base classes that are not marked
as "Mutable" (such as [`collections.abc.MutableSequence`][]), represent
objects that may or may not be mutable. The type hints in this module
represent the *read-only* interface of a collection: they expose no mutating
methods, so a value typed as one of them cannot be mutated through that type.

!!! note

    Structural typing cannot assert the *absence* of a method, so a concrete
    mutable object (e.g. a `#!python list`) may still satisfy these protocols
    structurally. When a hard guarantee is required, annotate with a concrete
    immutable type instead (e.g. `#!python Tuple`, `#!python frozenset` or
    [`types.MappingProxyType`][]).
"""
__all__ = ["ImmutableSequence", "ImmutableSet", "ImmutableMapping"]

# Import stdlib so that mkdocstring correctly resolves cross-references
import collections.abc  # noqa: F401

import typing_extensions as tx

from ._internal.typevars.co import K as K_co
from ._internal.typevars.co import T as T_co
from ._internal.typevars.inv import K as K_inv
from .collections import Collection, Mapping, Set


@tx.runtime_checkable
class ImmutableSequence(Collection[T_co], tx.Protocol[T_co]):
    """A read-only [`collections.abc.Sequence`][].

    Unlike [`Sequence`][bagof.hints.collections.Sequence] this does not require
    ``__reversed__``, so a canonical immutable `#!python Tuple` satisfies it.
    """

    def __getitem__(self, index: int) -> T_co: ...

    def index(self, value: object, start: int = ..., stop: int = ...) -> int:
        ...

    def count(self, value: object) -> int: ...


@tx.runtime_checkable
class ImmutableSet(Set[K_co], tx.Protocol[K_co]):
    """A read-only [`collections.abc.Set`][] (e.g. a `#!python frozenset`)."""

    ...


@tx.runtime_checkable
class ImmutableMapping(Mapping[K_inv, T_co], tx.Protocol[K_inv, T_co]):
    """A read-only [`collections.abc.Mapping`][].

    For example, a [`types.MappingProxyType`][].
    """

    ...
