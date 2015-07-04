class BaseMatcher(object):
    """The base class for pdbuddy matchers."""

    def match(self, frame, event, arg):
        raise NotImplementedError(
            'Subclasses need to implement the match method')
