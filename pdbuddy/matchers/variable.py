from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class VariableMatcher(BaseMatcher):

    def __init__(self, variable_name, match_func):
        self.variable_name = variable_name
        self.match_func = match_func

    def __call__(self, frame, event, arg):
        if self.variable_name in frame.f_locals:
            return self.match_func(frame.f_locals[self.variable_name])
        return False


class VariableValueMatcher(VariableMatcher):

    def __init__(self, variable_name, variable_value):
        super(VariableValueMatcher, self).__init__(
            variable_name, lambda value: variable_value == value)
