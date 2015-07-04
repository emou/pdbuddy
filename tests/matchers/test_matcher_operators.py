from __future__ import absolute_import

import pytest
from doubles import allow, InstanceDouble

from pdbuddy.matchers import BaseMatcher
from pdbuddy.matchers.matcher_operators import AndMatcher, BinaryMatcher, OrMatcher


def test_init_accepts_two_matchers():
    m1, m2 = object(), object()
    matcher = BinaryMatcher(m1, m2)
    assert matcher.matcher1 is m1
    assert matcher.matcher2 is m2


def test_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        assert BinaryMatcher(object(), object())(object(), object(), object())


def const_matcher(val):
    false_matcher = InstanceDouble('pdbuddy.matchers.base.BaseMatcher')
    allow(false_matcher).__call__.and_return(val)
    return false_matcher


@pytest.fixture
def true_matcher():
    return const_matcher(True)


@pytest.fixture
def false_matcher():
    return const_matcher(False)


def test_sanity(true_matcher, false_matcher):
    assert true_matcher(object(), object(), object()) is True
    assert false_matcher(object(), object(), object()) is False


def test_or_matcher_true_false(true_matcher, false_matcher):
    assert OrMatcher(true_matcher, false_matcher)(
        object(), object(), object()) is True


def test_or_matcher_false_true(true_matcher, false_matcher):
    assert OrMatcher(false_matcher, true_matcher)(
        object(), object(), object()) is True


def test_or_matcher_false_false(false_matcher):
    assert OrMatcher(false_matcher, false_matcher)(
        object(), object(), object()) is False


def test_or_matcher_true_true(true_matcher):
    assert OrMatcher(true_matcher, true_matcher)(
        object(), object(), object()) is True


def test_and_matcher_true_false(true_matcher, false_matcher):
    assert AndMatcher(true_matcher, false_matcher)(
        object(), object(), object()) is False


def test_and_matcher_false_true(true_matcher, false_matcher):
    assert AndMatcher(false_matcher, true_matcher)(
        object(), object(), object()) is False


def test_and_matcher_false_false(false_matcher):
    assert AndMatcher(false_matcher, false_matcher)(
        object(), object(), object()) is False


def test_and_matcher_true_true(true_matcher):
    assert AndMatcher(true_matcher, true_matcher)(
        object(), object(), object()) is True


def test_or_operator():
    m1 = BaseMatcher()
    m2 = BaseMatcher()

    or_matcher = m1 | m2
    assert isinstance(or_matcher, OrMatcher)
    assert or_matcher.matcher1 is m1
    assert or_matcher.matcher2 is m2


def test_and_operator():
    m1 = BaseMatcher()
    m2 = BaseMatcher()

    or_matcher = m1 & m2
    assert isinstance(or_matcher, AndMatcher)
    assert or_matcher.matcher1 is m1
    assert or_matcher.matcher2 is m2
