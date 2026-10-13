from __future__ import annotations

from typing import Any

import pytest

import humanize


@pytest.mark.parametrize("value", [3, "x", None, 0, 1.5, [1, 2], {"a": 1}])
def test_noop_returns_argument_unchanged(value: Any) -> None:
    assert humanize.noop(value) is value


def test_noop_exported_from_package_root() -> None:
    from humanize import noop

    assert "noop" in humanize.__all__
    assert noop(3) == 3
    assert noop("x") == "x"
    assert noop(None) is None
