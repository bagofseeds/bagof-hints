"""
Hints for [`numpy`][] arrays and data types.

!!! note
    This module is **not** imported by `bagof.hints`. Import it explicitly:

    ```python
    from bagof.hints import numpy as npt
    ```

    Importing it does not import numpy either: each numpy hint is resolved
    on first access (e.g., `npt.ndarray`), which is when numpy is imported.
    The library-agnostic protocols are available without importing numpy.

    It stays usable when numpy is absent, in which case the array types
    degrade to empty generic stubs, so that annotations still evaluate.
"""
__all__ = [
    "ArrayProtocol",
    "ArrayNamespace",
    "DTypeProtocol",
    "ArrayLike",
    "DTypeLike",
    "dtype",
    "ndarray",
    "NDArray",
    "typevars",
]

import typing_extensions as tx

from .._internal.lazy import lazy_attributes
from ..array import (  # noqa: F401
    ArrayNamespace,
    ArrayProtocol,
    DTypeProtocol,
)
from . import typevars

if tx.TYPE_CHECKING:
    # Import numpy so mkdocstrings resolves the `numpy.*` / `numpy.typing.*`
    # cross-references in the docstrings.
    import numpy  # noqa: F401, I001
    import numpy.typing  # noqa: F401

    # Not sorted: the docs list members in import order.
    from .._internal.numpy.arrays import (
        dtype,
        ndarray,
        NDArray,
        ArrayLike,
        DTypeLike,
    )

else:
    __getattr__, __dir__ = lazy_attributes(
        __name__,
        dict.fromkeys(
            ["dtype", "ndarray", "NDArray", "ArrayLike", "DTypeLike"],
            "bagof.hints._internal.numpy.arrays",
        ),
    )
