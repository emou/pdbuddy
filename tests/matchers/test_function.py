from __future__ import absolute_import

from pdbuddy.matchers.function import FunctionMatcher
from pdbuddy.trace_context import TraceContext


def test_true():
    assert FunctionMatcher(lambda *args: True)(
        TraceContext(object(), object(), object()))


def test_false():
    assert FunctionMatcher(lambda *args: True)(
        TraceContext(object(), object(), object()))
