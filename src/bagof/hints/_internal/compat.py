import typing_extensions as tx

__all__ = ["NoneType", "UnionType"]

# ``types.NoneType`` / ``types.UnionType`` only exist on Python 3.10+, so they
# are imported defensively at runtime. For type checking, ``NoneType`` is only
# ever used as a TypeVar bound meaning "the ``None`` type"; aliasing it to
# ``None`` keeps that valid across every target version (importing the real
# ``types.NoneType`` triggers mypy's ``valid-type`` error on 3.10+).
if tx.TYPE_CHECKING:
    NoneType: tx.TypeAlias = None
    UnionType: tx.TypeAlias = tx.Any

else:
    try:
        from types import NoneType
    except ImportError:  # pragma: no cover
        NoneType = type(None)

    try:
        from types import UnionType
    except ImportError:  # pragma: no cover
        UnionType = tx.Union

# NOTE: array libraries (numpy, cupy, dask) are deliberately *not* imported
# here. This module is imported eagerly by ``typevars``, so any array import
# would run on every ``import bagof.hints``. They are guarded inside the
# ``hints.numpy`` / ``hints.cupy`` / ``hints.dask`` packages instead, which
# are only imported on demand (see ``bagof.hints.__getattr__``).
