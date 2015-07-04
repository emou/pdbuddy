from __future__ import absolute_import

from pdbuddy import Tracer


def test_returns_itself():
    tracer = Tracer([])
    assert tracer(object(), 'call', object()) == tracer
