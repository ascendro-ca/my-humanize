"""Miscellaneous helpers."""

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
        value: Any value.

    Returns:
        The same object that was passed in.
    """
    return set(value) if isinstance(value, set) else value  # type: ignore[return-value]
