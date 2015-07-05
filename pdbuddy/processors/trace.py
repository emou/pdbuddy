from __future__ import absolute_import

from pdbuddy.formatters import SimpleFormatter
from pdbuddy.matchers import AnyMatcher
from pdbuddy.trace_context import TraceContext


class TraceProcessor(object):
    """Emits trace events during program execution.

    Generally a tracer that prints all matching events as per `sys.settrace`.
    """

    _ctx_class = TraceContext

    def __init__(self, matcher=None, formatter=None):
        if matcher is None:
            matcher = AnyMatcher()
        self.matcher = matcher

        if formatter is None:
            formatter = SimpleFormatter()
        self.formatter = formatter

    def __call__(self, frame, event, arg):
        context = self._ctx_class(frame, event, arg)
        if self.matcher(context):
            return self.formatter(frame, event, arg)
