class BaseMatcher(object):
    """The base class for pdbuddy matchers."""

    def __call__(self, frame, event, arg):
        raise NotImplementedError(
            'Subclasses need to implement the match method')
