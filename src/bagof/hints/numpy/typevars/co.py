"""
Covariant numpy TypeVars.

Importing this module does not import numpy: its TypeVars are resolved on
first access, which is when numpy is imported.
"""

import typing_extensions as tx

from ..._internal.lazy import lazy_attributes

if tx.TYPE_CHECKING:
    __all__ = ["DTYPE", "DTYPELIKE"]

    from ..._internal.numpy.typevars.co import DTYPE, DTYPELIKE

else:
    # ``__all__`` is lazy as well, since which TypeVars exist depends on
    # whether numpy is installed.
    __getattr__, __dir__ = lazy_attributes(
        __name__,
        dict.fromkeys(
            ["__all__", "DTYPE", "DTYPELIKE"],
            "bagof.hints._internal.numpy.typevars.co",
        ),
    )
