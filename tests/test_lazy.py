"""Unit tests for the lazy module attributes helper."""

from __future__ import annotations

import sys
import types

import pytest

from bagof.hints import json
from bagof.hints._internal.lazy import lazy_attributes


def test_lazy_all_is_resolved_on_access(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = types.ModuleType("bagof_hints_test_lazy")
    monkeypatch.setitem(sys.modules, module.__name__, module)
    getattr_, dir_ = lazy_attributes(
        module.__name__,
        dict.fromkeys(["__all__", "JSON", "MISSING"], json.__name__),
    )
    # Until ``__all__`` is resolved, ``__dir__`` lists the lazy names...
    assert dir_() == ["JSON", "MISSING"]
    assert "__all__" not in vars(module)
    # ... resolving one binds its loaded siblings, ``__all__`` included ...
    assert getattr_("JSON") is json.JSON
    assert vars(module)["__all__"] is json.__all__
    # ... after which ``__dir__`` lists ``__all__``.
    assert dir_() == sorted(json.__all__)
    # Names absent from their source, or unknown, raise.
    with pytest.raises(AttributeError):
        getattr_("MISSING")
    with pytest.raises(AttributeError):
        getattr_("unknown")
