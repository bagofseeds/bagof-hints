"""Import smoke tests."""

import importlib


def test_hints_submodule_is_importable() -> None:
    """The hints package should be importable after installation."""
    module = importlib.import_module("bagof.hints")
    assert module is not None
