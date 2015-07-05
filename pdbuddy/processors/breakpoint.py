from __future__ import absolute_import

from pdbuddy.trace_context import TraceContext


class BreakpointProcessor(object):
    """Adds a breakpoint when a matcher matches an trace event.

    Note this is just experimental and only supports adding a single breakpoint as the debugger
    overrides our `sys.settrace` function.
    """

    _ctx_class = TraceContext

    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, frame, event, arg):
        context = self._ctx_class(frame, event, arg)

        if self.matcher(context):
            # Importing ipdb has some side-effects so do it when it is actually needed
            try:
                import ipdb as db
            except ImportError:
                import pdb as db

            # TODO: Investigate `pdb.Pdb`'s `set_break` method.
            # TODO: Restore our tracing after coming back from the debuger
            # (currently this supports only one break).
            db.set_trace()
