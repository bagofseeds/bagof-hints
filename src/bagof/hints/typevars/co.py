__all__ = [
    "T",
    "K",
    "OBJECT",
    "TYPE",
    "NONE",
    "STR",
    "BYTES",
    "BOOL",
    "INT",
    "FLOAT",
    "COMPLEX",
    "INTEGRAL",
    "REAL",
    "NUMBER",
    "CONTAINER",
    "HASHABLE",
    "ITERABLE",
    "ITERATOR",
    "REVERSIBLE",
    "GENERATOR",
    "SIZED",
    "COLLECTION",
    "SEQUENCE",
    "MUTABLE_SEQUENCE",
    "SET",
    "MUTABLE_SET",
    "MAPPING",
    "MUTABLE_MAPPING",
    "AWAITABLE",
    "BUFFER",
    "LIST",
    "TUPLE",
    "DICT",
]

import numbers

import typing_extensions as tx

from .._internal.compat import NoneType
from .._internal.typevars.co import K, T

OBJECT = tx.TypeVar("OBJECT", covariant=True, bound=object)
"""A covariant TypeVar for objects."""

TYPE = tx.TypeVar("TYPE", covariant=True, bound=type)
"""A covariant TypeVar for types."""

NONE = tx.TypeVar("NONE", covariant=True, bound=NoneType)
"""A covariant TypeVar for None values."""

STR = tx.TypeVar("STR", covariant=True, bound=str)
"""A covariant TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", covariant=True, bound=bytes)
"""A covariant TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", covariant=True, bound=bool)
"""A covariant TypeVar for booleans."""

INT = tx.TypeVar("INT", covariant=True, bound=int)
"""A covariant TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", covariant=True, bound=float)
"""A covariant TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", covariant=True, bound=complex)
"""A covariant TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", covariant=True, bound=numbers.Integral)
"""A covariant TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", covariant=True, bound=numbers.Real)
"""A covariant TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", covariant=True, bound=numbers.Number)
"""A covariant TypeVar for numeric values."""

CONTAINER = tx.TypeVar("CONTAINER", covariant=True, bound=tx.Container[tx.Any])
"""A covariant TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", covariant=True, bound=tx.Hashable)
"""A covariant hashable TypeVar."""

ITERABLE = tx.TypeVar("ITERABLE", covariant=True, bound=tx.Iterable[tx.Any])
"""A covariant TypeVar for iterables."""

ITERATOR = tx.TypeVar("ITERATOR", covariant=True, bound=tx.Iterator[tx.Any])
"""A covariant TypeVar for iterators."""

REVERSIBLE = tx.TypeVar(
    "REVERSIBLE", covariant=True, bound=tx.Reversible[tx.Any])
"""A covariant TypeVar for reversibles."""

GENERATOR = tx.TypeVar(
    "GENERATOR", covariant=True, bound=tx.Generator[tx.Any, tx.Any, tx.Any])
"""A covariant TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", covariant=True, bound=tx.Sized)
"""A covariant TypeVar for sized objects."""

COLLECTION = tx.TypeVar(
    "COLLECTION", covariant=True, bound=tx.Collection[tx.Any])
"""A covariant TypeVar for collections."""

SEQUENCE = tx.TypeVar("SEQUENCE", covariant=True, bound=tx.Sequence[tx.Any])
"""A covariant TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", covariant=True, bound=tx.MutableSequence[tx.Any])
"""A covariant TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", covariant=True, bound=tx.Set[tx.Any])
"""A covariant TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", covariant=True, bound=tx.MutableSet[tx.Any])
"""A covariant TypeVar for mutable sets."""

MAPPING = tx.TypeVar(
    "MAPPING", covariant=True, bound=tx.Mapping[tx.Any, tx.Any])
"""A covariant TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING", covariant=True, bound=tx.MutableMapping[tx.Any, tx.Any])
"""A covariant TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar("AWAITABLE", covariant=True, bound=tx.Awaitable[tx.Any])
"""A covariant TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", covariant=True, bound=tx.Buffer)
"""A covariant TypeVar for buffers."""

LIST = tx.TypeVar("LIST", covariant=True, bound=tx.List[tx.Any])
"""A covariant TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", covariant=True, bound=tx.Tuple[tx.Any, ...])
"""A covariant TypeVar for tuples."""

DICT = tx.TypeVar("DICT", covariant=True, bound=tx.Dict[tx.Any, tx.Any])
"""A covariant TypeVar for dictionaries."""
