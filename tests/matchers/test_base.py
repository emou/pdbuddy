from __future__ import absolute_import

import pytest

from pdbuddy.matchers.base import BaseMatcher


def test_raises_not_implemented_error():
    with pytest.raises(NotImplementedError):
        assert BaseMatcher()(object(), object(), object())
