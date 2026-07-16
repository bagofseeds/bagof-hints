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

from .._internal.compat import NoneType, np, npt
from .._internal.typevars.contra import K, T

OBJECT = tx.TypeVar("OBJECT", contravariant=True, bound=object)
"""A contravariant TypeVar for objects."""

TYPE = tx.TypeVar("TYPE", contravariant=True, bound=type)
"""A contravariant TypeVar for types."""

NONE = tx.TypeVar("NONE", contravariant=True, bound=NoneType)
"""A contravariant TypeVar for None values."""

STR = tx.TypeVar("STR", contravariant=True, bound=str)
"""A contravariant TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", contravariant=True, bound=bytes)
"""A contravariant TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", contravariant=True, bound=bool)
"""A contravariant TypeVar for booleans."""

INT = tx.TypeVar("INT", contravariant=True, bound=int)
"""A contravariant TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", contravariant=True, bound=float)
"""A contravariant TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", contravariant=True, bound=complex)
"""A contravariant TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", contravariant=True, bound=numbers.Integral)
"""A contravariant TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", contravariant=True, bound=numbers.Real)
"""A contravariant TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", contravariant=True, bound=numbers.Number)
"""A contravariant TypeVar for numeric values."""

CONTAINER = tx.TypeVar(
    "CONTAINER", contravariant=True, bound=tx.Container[tx.Any])
"""A contravariant TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", contravariant=True, bound=tx.Hashable)
"""A contravariant hashable TypeVar."""

ITERABLE = tx.TypeVar(
    "ITERABLE", contravariant=True, bound=tx.Iterable[tx.Any])
"""A contravariant TypeVar for iterables."""

ITERATOR = tx.TypeVar(
    "ITERATOR", contravariant=True, bound=tx.Iterator[tx.Any])
"""A contravariant TypeVar for iterators."""

REVERSIBLE = tx.TypeVar(
    "REVERSIBLE", contravariant=True, bound=tx.Reversible[tx.Any])
"""A contravariant TypeVar for reversibles."""

GENERATOR = tx.TypeVar(
    "GENERATOR",
    contravariant=True,
    bound=tx.Generator[tx.Any, tx.Any, tx.Any],
)
"""A contravariant TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", contravariant=True, bound=tx.Sized)
"""A contravariant TypeVar for sized objects."""

COLLECTION = tx.TypeVar(
    "COLLECTION", contravariant=True, bound=tx.Collection[tx.Any])
"""A contravariant TypeVar for collections."""

SEQUENCE = tx.TypeVar(
    "SEQUENCE", contravariant=True, bound=tx.Sequence[tx.Any])
"""A contravariant TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", contravariant=True, bound=tx.MutableSequence[tx.Any])
"""A contravariant TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", contravariant=True, bound=tx.Set[tx.Any])
"""A contravariant TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", contravariant=True, bound=tx.MutableSet[tx.Any])
"""A contravariant TypeVar for mutable sets."""

MAPPING = tx.TypeVar(
    "MAPPING", contravariant=True, bound=tx.Mapping[tx.Any, tx.Any])
"""A contravariant TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING",
    contravariant=True,
    bound=tx.MutableMapping[tx.Any, tx.Any],
)
"""A contravariant TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar(
    "AWAITABLE", contravariant=True, bound=tx.Awaitable[tx.Any])
"""A contravariant TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", contravariant=True, bound=tx.Buffer)
"""A contravariant TypeVar for buffers."""

LIST = tx.TypeVar("LIST", contravariant=True, bound=tx.List[tx.Any])
"""A contravariant TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", contravariant=True, bound=tx.Tuple[tx.Any, ...])
"""A contravariant TypeVar for tuples."""

DICT = tx.TypeVar("DICT", contravariant=True, bound=tx.Dict[tx.Any, tx.Any])
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
