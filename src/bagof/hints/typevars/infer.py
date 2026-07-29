# mypy does not support the ``infer_variance`` argument to ``TypeVar()``
# in the legacy call form (it is only understood via PEP 695 class
# syntax), so it emits a spurious ``[misc]`` error for every TypeVar
# declared here. pyright and the typing_extensions runtime handle it
# correctly.
# mypy: disable-error-code="misc"
"""
TypeVars with inferred variance.

These are declared with `#!python infer_variance=True`, so the variance
is not fixed up front: the type checker derives it for each generic class
separately, from how the class actually uses the parameter. That makes a
single TypeVar reusable across classes that would otherwise need the
covariant, contravariant and invariant flavours.

Variance is only ever *inferred* per generic class or protocol
definition; it says nothing about the TypeVar in isolation.

Every TypeVar here carries an upper *bound* (not a set of value
constraints), so it can be solved for any subtype of that bound, and
never for an unrelated type.
"""
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
from .._internal.typevars.infer import K, T

OBJECT = tx.TypeVar("OBJECT", infer_variance=True, bound=object)
"""An inferred-variance TypeVar for objects."""

TYPE = tx.TypeVar("TYPE", infer_variance=True, bound=type)
"""An inferred-variance TypeVar for types."""

NONE = tx.TypeVar("NONE", infer_variance=True, bound=NoneType)
"""An inferred-variance TypeVar for None values."""

STR = tx.TypeVar("STR", infer_variance=True, bound=str)
"""An inferred-variance TypeVar for strings."""

BYTES = tx.TypeVar("BYTES", infer_variance=True, bound=bytes)
"""An inferred-variance TypeVar for bytes."""

BOOL = tx.TypeVar("BOOL", infer_variance=True, bound=bool)
"""An inferred-variance TypeVar for booleans."""

INT = tx.TypeVar("INT", infer_variance=True, bound=int)
"""An inferred-variance TypeVar for (builtin) ints."""

FLOAT = tx.TypeVar("FLOAT", infer_variance=True, bound=float)
"""An inferred-variance TypeVar for (builtin) floats."""

COMPLEX = tx.TypeVar("COMPLEX", infer_variance=True, bound=complex)
"""An inferred-variance TypeVar for (builtin) complex numbers."""

INTEGRAL = tx.TypeVar("INTEGRAL", infer_variance=True, bound=numbers.Integral)
"""An inferred-variance TypeVar for integral numbers."""

REAL = tx.TypeVar("REAL", infer_variance=True, bound=numbers.Real)
"""An inferred-variance TypeVar for real numbers."""

NUMBER = tx.TypeVar("NUMBER", infer_variance=True, bound=numbers.Number)
"""An inferred-variance TypeVar for numeric values."""

CONTAINER = tx.TypeVar(
    "CONTAINER", infer_variance=True, bound=tx.Container[tx.Any])
"""An inferred-variance TypeVar for containers."""

HASHABLE = tx.TypeVar("HASHABLE", infer_variance=True, bound=tx.Hashable)
"""An inferred-variance TypeVar for hashable objects."""

ITERABLE = tx.TypeVar(
    "ITERABLE", infer_variance=True, bound=tx.Iterable[tx.Any])
"""An inferred-variance TypeVar for iterables."""

ITERATOR = tx.TypeVar(
    "ITERATOR", infer_variance=True, bound=tx.Iterator[tx.Any])
"""An inferred-variance TypeVar for iterators."""

REVERSIBLE = tx.TypeVar(
    "REVERSIBLE", infer_variance=True, bound=tx.Reversible[tx.Any])
"""An inferred-variance TypeVar for reversibles."""

GENERATOR = tx.TypeVar(
    "GENERATOR",
    infer_variance=True,
    bound=tx.Generator[tx.Any, tx.Any, tx.Any],
)
"""An inferred-variance TypeVar for generators."""

SIZED = tx.TypeVar("SIZED", infer_variance=True, bound=tx.Sized)
"""An inferred-variance TypeVar for sized objects."""

COLLECTION = tx.TypeVar(
    "COLLECTION", infer_variance=True, bound=tx.Collection[tx.Any])
"""An inferred-variance TypeVar for collections."""

SEQUENCE = tx.TypeVar(
    "SEQUENCE", infer_variance=True, bound=tx.Sequence[tx.Any])
"""An inferred-variance TypeVar for sequences."""

MUTABLE_SEQUENCE = tx.TypeVar(
    "MUTABLE_SEQUENCE", infer_variance=True, bound=tx.MutableSequence[tx.Any])
"""An inferred-variance TypeVar for mutable sequences."""

SET = tx.TypeVar("SET", infer_variance=True, bound=tx.Set[tx.Any])
"""An inferred-variance TypeVar for sets."""

MUTABLE_SET = tx.TypeVar(
    "MUTABLE_SET", infer_variance=True, bound=tx.MutableSet[tx.Any])
"""An inferred-variance TypeVar for mutable sets."""

MAPPING = tx.TypeVar(
    "MAPPING", infer_variance=True, bound=tx.Mapping[tx.Any, tx.Any])
"""An inferred-variance TypeVar for mappings."""

MUTABLE_MAPPING = tx.TypeVar(
    "MUTABLE_MAPPING",
    infer_variance=True,
    bound=tx.MutableMapping[tx.Any, tx.Any],
)
"""An inferred-variance TypeVar for mutable mappings."""

AWAITABLE = tx.TypeVar(
    "AWAITABLE", infer_variance=True, bound=tx.Awaitable[tx.Any])
"""An inferred-variance TypeVar for awaitables."""

BUFFER = tx.TypeVar("BUFFER", infer_variance=True, bound=tx.Buffer)
"""An inferred-variance TypeVar for buffers."""

LIST = tx.TypeVar("LIST", infer_variance=True, bound=tx.List[tx.Any])
"""An inferred-variance TypeVar for lists."""

TUPLE = tx.TypeVar("TUPLE", infer_variance=True, bound=tx.Tuple[tx.Any, ...])
"""An inferred-variance TypeVar for tuples."""

DICT = tx.TypeVar("DICT", infer_variance=True, bound=tx.Dict[tx.Any, tx.Any])
"""An inferred-variance TypeVar for dictionaries."""
