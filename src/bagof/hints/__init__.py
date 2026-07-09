"""Reusable typing hints for Python projects."""
__all__ = ["__version__"]

import os

import typing_extensions as tx

try:
    from ._version import __version__
except ImportError:  # pragma: no cover
    __version__ = "0+unknown"


from . import builtin
from . import collections
from . import flexi
from . import immutable
from . import json
from . import strings
from . import typevars
from . import unpackable

from .builtin import *
from .collections import *
from .flexi import *
from .immutable import *
from .json import *
from .strings import *
from .typevars import *
from .unpackable import *

from .builtin import __all__ as __all_builtin
from .collections import __all__ as __all_collections
from .flexi import __all__ as __all_flexi
from .immutable import __all__ as __all_immutable
from .json import __all__ as __all_json
from .strings import __all__ as __all_strings
from .typevars import __all__ as __all_typevars
from .unpackable import __all__ as __all_unpackable

__all__ += __all_builtin
__all__ += __all_collections
__all__ += __all_flexi
__all__ += __all_immutable
__all__ += __all_json
__all__ += __all_strings
__all__ += __all_typevars
__all__ += __all_unpackable
