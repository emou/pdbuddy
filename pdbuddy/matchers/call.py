from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class CallMatcher(BaseMatcher):

    def __call__(self, context):
        return context.is_call()
