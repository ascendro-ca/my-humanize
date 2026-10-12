"""Miscellaneous helpers."""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")

__all__ = ["noop"]


def noop(value: T) -> T:
    """Return the argument unchanged.

    Examples:
        >>> noop(3)
        3
        >>> noop("x")
        'x'
        >>> noop(None) is None
        True

    Args:
        value (Any): Any value.

    Returns:
        Any: The same object that was passed in.
    """
    return value
