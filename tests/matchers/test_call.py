from __future__ import absolute_import

from pdbuddy.matchers.call import CallMatcher


def test_matches_call_event():
    assert CallMatcher()(object(), 'call', object())


def test_doesnt_match_line_event():
    assert CallMatcher()(object(), 'line', object()) is False
