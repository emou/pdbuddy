from __future__ import absolute_import


class BaseMatcher(object):
    """The base class for pdbuddy matchers."""

    def __call__(self, frame, event, arg):
        raise NotImplementedError(
            'Subclasses need to implement the match method')

    def __or__(self, other):
        from pdbuddy.matchers.matcher_operators import OrMatcher
        return OrMatcher(self, other)

    def __and__(self, other):
        from pdbuddy.matchers.matcher_operators import AndMatcher
        return AndMatcher(self, other)
