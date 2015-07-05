from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class BinaryMatcher(BaseMatcher):

    def __init__(self, matcher1, matcher2):
        self.matcher1 = matcher1
        self.matcher2 = matcher2


class AndMatcher(BinaryMatcher):

    def __call__(self, context):
        return self.matcher1(context) and self.matcher2(context)


class OrMatcher(BinaryMatcher):

    def __call__(self, context):
        return self.matcher1(context) or self.matcher2(context)


class InvertMatcher(BaseMatcher):

    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, context):
        return not self.matcher(context)
