import typing_extensions as tx

__all__ = ["NoneType", "UnionType", "np", "npt"]

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

# numpy is an optional dependency.
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
