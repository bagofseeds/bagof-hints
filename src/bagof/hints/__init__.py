"""
Reusable typing hints for Python projects.

Modules
-------
builtin
    Builtin types (such as builtin subsets of [collections.abc][]).
collections
    Protocols that are compatible with [collections.abc][].
flexi
    Flexible "type-like" for use in converters.
immutable
    Immutable collections.
json
    Types related to JSON (de)serialization.
strings
    String-like objects."
typevars
    Reusable TypeVars.
unpackable
    Objects unpackable into keyword arguments.
"""
__all__ = [
    "__version__",
    "builtin",
    "collections",
    "flexi",
    "immutable",
    "json",
    "strings",
    "typevars",
    "unpackable",
]

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0+unknown"

from . import (
    builtin,
    collections,
    flexi,
    immutable,
    json,
    strings,
    typevars,
    unpackable,
)
from .builtin import *  # noqa: F401, F403
from .builtin import __all__ as __all_builtin
from .collections import *  # noqa: F401, F403
from .collections import __all__ as __all_collections
from .flexi import *  # noqa: F401, F403
from .flexi import __all__ as __all_flexi
from .immutable import *  # noqa: F401, F403
from .immutable import __all__ as __all_immutable
from .json import *  # noqa: F401, F403
from .json import __all__ as __all_json
from .strings import *  # noqa: F401, F403
from .strings import __all__ as __all_strings
from .typevars import *  # noqa: F401, F403
from .typevars import __all__ as __all_typevars
from .unpackable import *  # noqa: F401, F403
from .unpackable import __all__ as __all_unpackable

__all__ += __all_builtin
__all__ += __all_collections
__all__ += __all_flexi
__all__ += __all_immutable
__all__ += __all_json
__all__ += __all_strings
__all__ += __all_typevars
__all__ += __all_unpackable
