from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class FunctionMatcher(BaseMatcher):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(*args)
