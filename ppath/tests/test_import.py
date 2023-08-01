"""Test ppath."""

import ppath


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(ppath.__name__, str)
