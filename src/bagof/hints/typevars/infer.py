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
from .._internal.typevars.infer import K, T

OBJECT = tx.TypeVar("OBJECT", infer_variance=True, bound=object)
"""A inferable TypeVar for objects."""

TYPE = tx.TypeVar("TYPE", infer_variance=True, bound=type)
"""A inferable TypeVar for types."""

NONE = tx.TypeVar("NONE", infer_variance=True, bound=NoneType)
"""A inferable TypeVar for None values."""

STR = tx.TypeVar("STR", infer_variance=True, bound=str)
"""A inferable TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", infer_variance=True, bound=bytes)
"""A inferable TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", infer_variance=True, bound=bool)
"""A inferable TypeVar for booleans."""

INT = tx.TypeVar("INT", infer_variance=True, bound=int)
"""A inferable TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", infer_variance=True, bound=float)
"""A inferable TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", infer_variance=True, bound=complex)
"""A inferable TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", infer_variance=True, bound=numbers.Integral)
"""A inferable TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", infer_variance=True, bound=numbers.Real)
"""A inferable TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", infer_variance=True, bound=numbers.Number)
"""A inferable TypeVar for numeric values."""

CONTAINER = tx.TypeVar("CONTAINER", infer_variance=True, bound=tx.Container)
"""A inferable TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", infer_variance=True, bound=tx.Hashable)
"""A inferable hashable TypeVar."""

ITERABLE = tx.TypeVar("ITERABLE", infer_variance=True, bound=tx.Iterable)
"""A inferable TypeVar for iterables."""

ITERATOR = tx.TypeVar("ITERATOR", infer_variance=True, bound=tx.Iterator)
"""A inferable TypeVar for iterators."""

REVERSIBLE = tx.TypeVar("REVERSIBLE", infer_variance=True, bound=tx.Reversible)
"""A inferable TypeVar for reversibles."""

GENERATOR = tx.TypeVar("GENERATOR", infer_variance=True, bound=tx.Generator)
"""A inferable TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", infer_variance=True, bound=tx.Sized)
"""A inferable TypeVar for sized objects."""

COLLECTION = tx.TypeVar("COLLECTION", infer_variance=True, bound=tx.Collection)
"""A inferable TypeVar for collections."""

SEQUENCE = tx.TypeVar("SEQUENCE", infer_variance=True, bound=tx.Sequence)
"""A inferable TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", infer_variance=True, bound=tx.MutableSequence)
"""A inferable TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", infer_variance=True, bound=tx.Set)
"""A inferable TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", infer_variance=True, bound=tx.MutableSet)
"""A inferable TypeVar for mutable sets."""

MAPPING = tx.TypeVar("MAPPING", infer_variance=True, bound=tx.Mapping)
"""A inferable TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING", infer_variance=True, bound=tx.MutableMapping)
"""A inferable TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar("AWAITABLE", infer_variance=True, bound=tx.Awaitable)
"""A inferable TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", infer_variance=True, bound=tx.Buffer)
"""A inferable TypeVar for buffers."""

LIST = tx.TypeVar("LIST", infer_variance=True, bound=tx.List)
"""A inferable TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", infer_variance=True, bound=tx.Tuple)
"""A inferable TypeVar for tuples."""

DICT = tx.TypeVar("DICT", infer_variance=True, bound=tx.Dict)
"""A inferable TypeVar for dictionaries."""

if tx.TYPE_CHECKING or np:
    DTYPE = tx.TypeVar("DTYPE", infer_variance=True, bound=np.dtype)
    """A inferable TypeVar for numpy dtypes."""

    __all__.append("DTYPE")

if tx.TYPE_CHECKING or npt:
    DTYPELIKE = tx.TypeVar(
        "DTYPELIKE", infer_variance=True, bound=npt.DTypeLike)
    """
    A inferable TypeVar for things that can be converted to numpy dtypes.
    """

    __all__.append("DTYPELIKE")
