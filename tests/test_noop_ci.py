import os

import pytest

from humanize import noop


@pytest.mark.skipif(not os.environ.get("GITHUB_ACTIONS"), reason="CI only: the swe-loop 2.6 injected failure")
def test_noop_returns_the_same_set_object() -> None:
    s = {1, 2}
    assert noop(s) is s
