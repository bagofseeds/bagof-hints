"""
Guarded numpy imports for the [`bagof.hints.numpy`][] package.

This lives inside the ``hints.numpy`` package -- rather than in the shared
``hints._internal.compat`` -- precisely so that importing ``bagof.hints``
does not import numpy. It is only loaded once something under
``hints.numpy`` is imported.
"""
import typing_extensions as tx

__all__ = ["np", "npt"]

if tx.TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt

else:
    try:
        import numpy as np
    except ImportError:  # pragma: no cover
        np = None

    try:
        import numpy.typing as npt
    except ImportError:  # pragma: no cover
        npt = None
