from __future__ import absolute_import

from pdbuddy.matchers.base import BaseMatcher


class VariableMatcher(BaseMatcher):

    def __init__(self, variable_name, match_func):
        self.variable_name = variable_name
        self.match_func = match_func

    def __call__(self, context):
        if context.has_local_variable(self.variable_name):
            return self.match_func(context.get_local_variable(
                self.variable_name))
        return False


class VariableValueMatcher(VariableMatcher):

    def __init__(self, variable_name, variable_value):
        super(VariableValueMatcher, self).__init__(
            variable_name, lambda value: variable_value == value)
