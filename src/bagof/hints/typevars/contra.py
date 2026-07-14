__all__ = [
    "T",
    "K",
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

from .._internal.compat import NoneType, np, npt
from .._internal.typevars.contra import K, T

NONE = tx.TypeVar("NONE", contravariant=True, bound=NoneType)
"""A contravariant TypeVar for None values."""

STR = tx.TypeVar("STR", contravariant=True, bound=str)
"""A covariant TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", contravariant=True, bound=bytes)
"""A covariant TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", contravariant=True, bound=bool)
"""A covariant TypeVar for booleans."""

INT = tx.TypeVar("INT", contravariant=True, bound=int)
"""A covariant TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", contravariant=True, bound=float)
"""A covariant TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", contravariant=True, bound=complex)
"""A covariant TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", contravariant=True, bound=numbers.Integral)
"""A covariant TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", contravariant=True, bound=numbers.Real)
"""A covariant TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", contravariant=True, bound=numbers.Number)
"""A covariant TypeVar for numeric values."""

CONTAINER = tx.TypeVar("CONTAINER", contravariant=True, bound=tx.Container)
"""A covariant TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", contravariant=True, bound=tx.Hashable)
"""A covariant hashable TypeVar."""

ITERABLE = tx.TypeVar("ITERABLE", contravariant=True, bound=tx.Iterable)
"""A covariant TypeVar for iterables."""

ITERATOR = tx.TypeVar("ITERATOR", contravariant=True, bound=tx.Iterator)
"""A covariant TypeVar for iterators."""

REVERSIBLE = tx.TypeVar("REVERSIBLE", contravariant=True, bound=tx.Reversible)
"""A covariant TypeVar for reversibles."""

GENERATOR = tx.TypeVar("GENERATOR", contravariant=True, bound=tx.Generator)
"""A covariant TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", contravariant=True, bound=tx.Sized)
"""A covariant TypeVar for sized objects."""

COLLECTION = tx.TypeVar("COLLECTION", contravariant=True, bound=tx.Collection)
"""A covariant TypeVar for collections."""

SEQUENCE = tx.TypeVar("SEQUENCE", contravariant=True, bound=tx.Sequence)
"""A covariant TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", contravariant=True, bound=tx.MutableSequence)
"""A covariant TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", contravariant=True, bound=tx.Set)
"""A covariant TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", contravariant=True, bound=tx.MutableSet)
"""A covariant TypeVar for mutable sets."""

MAPPING = tx.TypeVar("MAPPING", contravariant=True, bound=tx.Mapping)
"""A covariant TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING", contravariant=True, bound=tx.MutableMapping)
"""A covariant TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar("AWAITABLE", contravariant=True, bound=tx.Awaitable)
"""A covariant TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", contravariant=True, bound=tx.Buffer)
"""A covariant TypeVar for buffers."""

LIST = tx.TypeVar("LIST", contravariant=True, bound=tx.List)
"""A contravariant TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", contravariant=True, bound=tx.Tuple)
"""A contravariant TypeVar for tuples."""

DICT = tx.TypeVar("DICT", contravariant=True, bound=tx.Dict)
"""A contravariant TypeVar for dictionaries."""

if tx.TYPE_CHECKING or np:
    DTYPE = tx.TypeVar("DTYPE", contravariant=True, bound=np.dtype)
    """A contravariant TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt:
    DTYPELIKE = tx.TypeVar(
        "DTYPELIKE", contravariant=True, bound=npt.DTypeLike)
    """
    A contravariant TypeVar for things that can be converted to numpy dtypes.
    """

    __all__.append("DTYPELIKE")
