# mypy does not support the ``infer_variance`` argument to ``TypeVar()``
# in the legacy call form (it is only understood via PEP 695 class
# syntax), so it emits a spurious ``[misc]`` error for every TypeVar
# declared here. pyright and the typing_extensions runtime handle it
# correctly.
# mypy: disable-error-code="misc"
__all__ = ["T", "K"]

import typing_extensions as tx

T = tx.TypeVar("T", default=tx.Any, infer_variance=True)
"""A TypeVar whose variance is inferred (with a compact name)."""

K = tx.TypeVar("K", bound=tx.Hashable, infer_variance=True)
"""An hashable TypeVar whose variance is inferred (with a compact name)."""
