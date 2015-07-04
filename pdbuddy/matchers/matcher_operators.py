from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class BinaryMatcher(BaseMatcher):

    def __init__(self, matcher1, matcher2):
        self.matcher1 = matcher1
        self.matcher2 = matcher2


class AndMatcher(BinaryMatcher):

    def __call__(self, *args):
        return self.matcher1(*args) and self.matcher2(*args)


class OrMatcher(BinaryMatcher):

    def __call__(self, *args):
        return self.matcher1(*args) or self.matcher2(*args)


class InvertMatcher(BaseMatcher):

    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, *args):
        return not self.matcher(*args)
