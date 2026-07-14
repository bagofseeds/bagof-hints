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
from .._internal.typevars.inv import K, T

OBJECT = tx.TypeVar("OBJECT", bound=object)
"""An invariant TypeVar for objects."""

TYPE = tx.TypeVar("TYPE", bound=type)
"""An invariant TypeVar for types."""

NONE = tx.TypeVar("NONE", infer_variance=True, bound=NoneType)
"""An invariant TypeVar for None values."""

STR = tx.TypeVar("STR", bound=str)
"""An invariant TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", bound=bytes)
"""An invariant TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", bound=bool)
"""An invariant TypeVar for booleans."""

INT = tx.TypeVar("INT", bound=int)
"""An invariant TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", bound=float)
"""An invariant TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", bound=complex)
"""An invariant TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", bound=numbers.Integral)
"""An invariant TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", bound=numbers.Real)
"""An invariant TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", bound=numbers.Number)
"""An invariant TypeVar for numeric values."""

CONTAINER = tx.TypeVar("CONTAINER", bound=tx.Container)
"""An invariant TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", bound=tx.Hashable)
"""An invariant hashable TypeVar."""

ITERABLE = tx.TypeVar("ITERABLE", bound=tx.Iterable)
"""An invariant TypeVar for iterables."""

ITERATOR = tx.TypeVar("ITERATOR", bound=tx.Iterator)
"""An invariant TypeVar for iterators."""

REVERSIBLE = tx.TypeVar("REVERSIBLE", bound=tx.Reversible)
"""An invariant TypeVar for reversibles."""

GENERATOR = tx.TypeVar("GENERATOR", bound=tx.Generator)
"""An invariant TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", bound=tx.Sized)
"""An invariant TypeVar for sized objects."""

COLLECTION = tx.TypeVar("COLLECTION", bound=tx.Collection)
"""An invariant TypeVar for collections."""

SEQUENCE = tx.TypeVar("SEQUENCE", bound=tx.Sequence)
"""An invariant TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", bound=tx.MutableSequence)
"""An invariant TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", bound=tx.Set)
"""An invariant TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", bound=tx.MutableSet)
"""An invariant TypeVar for mutable sets."""

MAPPING = tx.TypeVar("MAPPING", bound=tx.Mapping)
"""An invariant TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING", bound=tx.MutableMapping)
"""An invariant TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar("AWAITABLE", bound=tx.Awaitable)
"""An invariant TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", bound=tx.Buffer)
"""An invariant TypeVar for buffers."""

LIST = tx.TypeVar("LIST", bound=tx.List)
"""An invariant TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", bound=tx.Tuple)
"""An invariant TypeVar for tuples."""

DICT = tx.TypeVar("DICT", bound=tx.Dict)
"""An invariant TypeVar for dictionaries."""

if tx.TYPE_CHECKING or np:
    DTYPE = tx.TypeVar("DTYPE", bound=np.dtype)
    """An invariant TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt:
    DTYPELIKE = tx.TypeVar("DTYPELIKE", bound=npt.DTypeLike)
    """
    An invariant TypeVar for things that can be converted to numpy dtypes.
    """

    __all__.append("DTYPELIKE")
