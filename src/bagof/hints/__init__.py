"""
Reusable typing hints for Python projects.

Modules
-------
array
    :material-asterisk: Library-agnostic protocols for array-like objects.
builtin
    :material-asterisk: Builtin types (such as builtin subsets of
    [`collections.abc`][_abc]).
collections
    :material-asterisk: Protocols that are compatible with
    [`collections.abc`][_abc].
flexi
    :material-asterisk: Flexible "type-like" for use in converters.
json
    :material-asterisk: Types related to JSON (de)serialization.
strings
    :material-asterisk: String-like objects.
typevars
    :material-asterisk: Reusable TypeVars.
unpackable
    :material-asterisk: Objects unpackable into keyword arguments.
numpy
    :material-sleep: Hints for [`numpy`][_np] arrays and data types.
cupy
    :material-sleep: Hints for [`cupy`][_cp] arrays.
dask
    :material-sleep: Hints for [`dask.array`][_da] arrays.

!!! tip ":material-asterisk: Unpacked modules"
    Unpacked modules have all their symbols imported into the root module.
    For example, [`JSON`][bagof.hints.json.JSON] can be accessed via
    [`bagof.hints.json.JSON`][] **or** [`bagof.hints.JSON`][].

!!! tip ":material-sleep: Lazy modules"
    Lazy modules ([`numpy`][.numpy], [`cupy`][.cupy], [`dask`][.dask])
    are **not** imported by default, and importing them (or accessing
    them as `bagof.hints.<name>`) imports the corresponding array library.
    They stay importable when that library is absent.
"""

__all__ = [
    "__version__",
    "array",
    "builtin",
    "collections",
    "flexi",
    "json",
    "strings",
    "typevars",
    "unpackable",
    # Lazy submodules (see ``__getattr__``): named here so that they are
    # discoverable and importable, but *not* imported eagerly below. They
    # resolve dynamically, so static analysis cannot see them here.
    "numpy",  # noqa: F405
    "cupy",  # noqa: F405
    "dask",  # noqa: F405
]

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0+unknown"

# Import libs so that mkdocstring correctly resolves cross-references
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    import collections.abc as _abc  # noqa: F401

    import cupy as _cp  # noqa: F401
    import dask.array as _da  # noqa: F401
    import numpy as _np  # noqa: F401

from . import (
    array,
    builtin,
    collections,
    flexi,
    json,
    strings,
    typevars,
    unpackable,
)
from .array import *  # noqa: F401, F403
from .array import __all__ as __all_array
from .builtin import *  # noqa: F401, F403
from .builtin import __all__ as __all_builtin
from .collections import *  # noqa: F401, F403
from .collections import __all__ as __all_collections
from .flexi import *  # noqa: F401, F403
from .flexi import __all__ as __all_flexi
from .json import *  # noqa: F401, F403
from .json import __all__ as __all_json
from .strings import *  # noqa: F401, F403
from .strings import __all__ as __all_strings
from .typevars import *  # noqa: F401, F403
from .typevars import __all__ as __all_typevars
from .unpackable import *  # noqa: F401, F403
from .unpackable import __all__ as __all_unpackable

__all__ += __all_array
__all__ += __all_builtin
__all__ += __all_collections
__all__ += __all_flexi
__all__ += __all_json
__all__ += __all_strings
__all__ += __all_typevars
__all__ += __all_unpackable


# Submodules that import an array library, resolved lazily on attribute
# access (PEP 562) so that ``import bagof.hints`` never imports numpy, cupy
# or dask. ``from bagof.hints import numpy`` and ``import bagof.hints.numpy``
# both keep working through the normal import system.
_LAZY_MODULES = ("numpy", "cupy", "dask")


def __getattr__(name: str) -> object:
    if name in _LAZY_MODULES:
        import importlib

        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> "list":
    return sorted(__all__)
