from __future__ import annotations

from typing import Any

import pytest

import humanize


@pytest.mark.parametrize("value", [3, "x", None, 0, "", 1.5, [1, 2], {"a": 1}])
def test_noop(value: Any) -> None:
    assert humanize.noop(value) == value


def test_noop_returns_same_object() -> None:
    obj = [1, 2]
    assert humanize.noop(obj) is obj
    assert humanize.noop(None) is None


def test_noop_exported_from_root() -> None:
    from humanize import noop

    assert "noop" in humanize.__all__
    assert noop("x") == "x"
