"""
cupy array type, resolved lazily by [`bagof.hints.cupy`][].

Importing this module imports cupy (when installed), which is why the public
module only loads it once one of these hints is accessed.
"""
__all__ = [
    "ndarray",
    "NDArray",
]

import sys

import typing_extensions as tx

from .numpy.arrays import dtype
from .typevars.inv import DTYPE, SHAPE

if tx.TYPE_CHECKING:
    # Import the bare module so mkdocstrings resolves the `cupy.*`
    # cross-references in the docstrings below.
    import cupy  # noqa: F401
    import cupy as cp

else:
    try:
        import cupy as cp
    except ImportError:  # pragma: no cover
        cp = None


# Whether cupy's array type can be parametrised at runtime (see the note in
# ``_internal.numpy.arrays`` on the two gates; cupy mirrors numpy's behaviour).
_SUBSCRIPTABLE = (
    cp is not None
    and sys.version_info >= (3, 9)
    and hasattr(cp.ndarray, "__class_getitem__")
)


if tx.TYPE_CHECKING or _SUBSCRIPTABLE:  # pragma: no cover
    # cupy is not installable in CI (it needs a CUDA toolchain), so the
    # library-present branch is only ever type-checked, never run.
    ndarray = cp.ndarray
    """See [`cupy.ndarray`][]."""

else:

    class ndarray(tx.Generic[SHAPE, DTYPE]):  # type: ignore[no-redef]
        """A generic stub for [`cupy.ndarray`][]."""

        __module__ = "bagof.hints.cupy"


NDArray: tx.TypeAlias = ndarray[tx.Tuple[int, ...], dtype[DTYPE]]
"""A cupy array of arbitrary shape, parametrised by its data type."""
