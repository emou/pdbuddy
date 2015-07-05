from __future__ import absolute_import

from pdbuddy.matchers.match_any import AnyMatcher
from pdbuddy.trace_context import TraceContext


def test_matches_any():
    assert AnyMatcher()(TraceContext(object(), object(), object()))
