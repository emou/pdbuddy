from __future__ import absolute_import

from pdbuddy.matchers.call import CallMatcher
from pdbuddy.trace_context import TraceContext


def test_matches_call_event():
    assert CallMatcher()(TraceContext(object(), 'call', object())) is True


def test_doesnt_match_line_event():
    assert CallMatcher()(TraceContext(object(), 'line', object())) is False
