"""Miscellaneous helpers for humanize."""

from __future__ import annotations

from typing import TypeVar

T = TypeVar("T")


def noop(value: T) -> T:
    """Return the argument unchanged.

    Examples:
        ```pycon
        >>> noop(3)
        3
        >>> noop("x")
        'x'
        >>> noop(None) is None
        True

        ```

    Args:
        value (Any): Any value.

    Returns:
        Any: `value`, unchanged.
    """
    return value
