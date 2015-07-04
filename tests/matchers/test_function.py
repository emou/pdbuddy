from __future__ import absolute_import

from pdbuddy.matchers.function import FunctionMatcher


def test_true():
    assert FunctionMatcher(lambda *args: True)(
        object(), object(), object())


def test_false():
    assert FunctionMatcher(lambda *args: True)(
        object(), object(), object())
