import sys

import pytest

from humanize import noop


@pytest.mark.skipif(sys.platform != "linux", reason="Linux only, so CI only from a Mac: the swe-loop 2.6 injected failure")
def test_noop_returns_the_same_set_object() -> None:
    s = {1, 2}
    assert noop(s) is s
