from __future__ import absolute_import

from pdbuddy.matchers.match_any import AnyMatcher


def test_matches_any():
    assert AnyMatcher()(object(), object(), object())
