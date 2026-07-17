__all__ = ["T", "K", "SHAPE", "DTYPE"]

import typing_extensions as tx

T = tx.TypeVar("T", default=tx.Any)
"""An invariant TypeVar (with a compact name)."""

K = tx.TypeVar("K", bound=tx.Hashable)
"""An invariant hashable TypeVar (with a compact name)."""

SHAPE = tx.TypeVar("SHAPE", bound=tx.Tuple[tx.Any, ...])
"""An invariant TypeVar for array shapes (with a compact name)."""

# Unlike the public ``typevars.inv.DTYPE``, this one is *not* bound to
# ``np.dtype``, so it exists even when numpy is absent. It parametrises the
# array protocols and the stub array types, which must stay importable
# without any array library installed.
DTYPE = tx.TypeVar("DTYPE", bound=type)
"""An invariant TypeVar for array data types (with a compact name)."""
