from __future__ import absolute_import

from mock import Mock
import pytest

from pdbuddy.matchers.variable import VariableMatcher, VariableValueMatcher


@pytest.fixture
def frame():
    frame = Mock()
    frame.f_locals = {
        'bar': 13,
    }
    return frame


def test_matches(frame):
    assert VariableMatcher('bar', lambda bar: bar == 13)(frame, object(), object()) is True
    assert VariableMatcher('bar', lambda bar: bar > 12)(frame, object(), object()) is True


def test_doesnt_match(frame):
    assert VariableMatcher('bar', lambda bar: bar != 13)(frame, object(), object()) is False
    assert VariableMatcher('bar', lambda bar: bar < 12)(frame, object(), object()) is False


def test_nonexisting_var(frame):
    assert VariableMatcher('foo', lambda foo: True)(frame, object(), object()) is False
    assert VariableMatcher('foo', lambda foo: True)(frame, object(), object()) is False


def test_variable_value_matches(frame):
    assert VariableValueMatcher('bar', 13)(frame, object(), object()) is True


def test_variable_value_doesnt_match(frame):
    assert VariableValueMatcher('bar', 14)(frame, object(), object()) is False
