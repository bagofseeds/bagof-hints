"""
Guarded numpy imports for the [`bagof.hints.numpy`][] hints.

This lives in its own module -- rather than in the shared
``hints._internal.compat`` -- precisely so that importing ``bagof.hints``
(or ``bagof.hints.numpy``) does not import numpy. It is only loaded once a
numpy hint is accessed.
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
