from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class LineNumberMatcher(BaseMatcher):

    def __init__(self, line_number):
        self.line_number = line_number

    def __call__(self, context):
        return context.current_line == self.line_number
