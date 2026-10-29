"""
dask array type, resolved lazily by [`bagof.hints.dask`][].

Importing this module imports dask (when installed), which is why the public
module only loads it once one of these hints is accessed.
"""
__all__ = [
    "Array",
    "NDArray",
]

import sys

import typing_extensions as tx

from .numpy.arrays import dtype
from .typevars.inv import DTYPE, SHAPE

if tx.TYPE_CHECKING:
    # Import the bare module so mkdocstrings resolves the `dask.array.*`
    # cross-references in the docstrings below.
    import dask.array  # noqa: F401
    import dask.array as da

else:
    try:
        import dask.array as da
    except ImportError:  # pragma: no cover
        da = None


# Whether dask's array type can be parametrised at runtime (see the note in
# ``_internal.numpy.arrays`` on the two gates). dask's ``Array`` has no
# ``__class_getitem__`` at all today, so this is currently always False and
# the generic stub is used -- for `isinstance`, use the real
# ``dask.array.Array`` or the library-free
# [`ArrayProtocol`][bagof.hints.array.ArrayProtocol].
_SUBSCRIPTABLE = (
    da is not None
    and sys.version_info >= (3, 9)
    and hasattr(da.Array, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:  # pragma: no cover
    Array = da.Array
    """See [`dask.array.Array`][]."""

else:

    class Array(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`dask.array.Array`][]."""

        __module__ = "bagof.hints.dask"


NDArray: tx.TypeAlias = Array[tx.Tuple[int, ...], dtype[DTYPE]]
"""A dask array of arbitrary shape, parametrised by its data type."""
