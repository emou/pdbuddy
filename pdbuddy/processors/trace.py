from __future__ import absolute_import

from pdbuddy.matchers import AnyMatcher
from pdbuddy.formatters import SimpleFormatter


class TraceProcessor(object):
    """Emits trace events during program execution.

    Generally a tracer that prints all matching events as per `sys.settrace`.
    """

    def __init__(self, matcher=None, formatter=None):
        if matcher is None:
            matcher = AnyMatcher()
        self.matcher = matcher

        if formatter is None:
            formatter = SimpleFormatter()
        self.formatter = formatter

    def __call__(self, *args):
        if self.matcher(*args):
            return self.formatter(*args)
