"""Implementations of various matchers for pdbuddy

Matchers provide a convinience layer for filtering trace points. If a matcher
matches a call trace, that call will be processed. Otherwise it will be
ignored.
"""

from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher
from pdbuddy.matchers.call import CallMatcher
from pdbuddy.matchers.filename import FilenameMatcher
from pdbuddy.matchers.match_any import AnyMatcher
from pdbuddy.matchers.matcher_operators import AndMatcher, BinaryMatcher, OrMatcher
from pdbuddy.matchers.function import FunctionMatcher

__all__ = [
    'AndMatcher',
    'AnyMatcher',
    'BaseMatcher',
    'BinaryMatcher',
    'CallMatcher',
    'FilenameMatcher',
    'FunctionMatcher',
    'OrMatcher',
]
