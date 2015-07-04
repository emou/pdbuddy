from __future__ import absolute_import

try:
    import ipdb as db
except ImportError:
    import pdb as db


class BreakpointProcessor(object):
    """Adds a breakpoint when a matcher matches an trace event.

    Note this is just experimental and only supports adding a single breakpoint as the debugger
    overrides our `sys.settrace` function.
    """

    def __init__(self, matcher):
        self.matcher = matcher

    def __call__(self, *args):
        if self.matcher.match(*args):
            # TODO: Investigate `pdb.Pdb`'s `set_break` method.
            # TODO: Restore our tracing after coming back from the debuger
            # (currently this supports only one break).
            db.set_trace()
