from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class AnyMatcher(BaseMatcher):
    """A Matcher that matches any trace"""

    def __call__(self, frame, event, arg):
        return True
