from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class AnyMatcher(BaseMatcher):
    """A Matcher that matches any trace"""

    def match(self, *args):
        return True
