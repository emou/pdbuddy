from __future__ import absolute_import

import pytest

from mock import Mock
from pdbuddy.matchers.line_number import LineNumberMatcher
from pdbuddy.trace_context import TraceContext


@pytest.fixture
def frame():
    frame = Mock()
    frame.f_lineno = 21
    return frame


def test_matches_line_number(frame):
    assert LineNumberMatcher(21)(TraceContext(frame, object(), object())) is True


def test_doesnt_match_line_number(frame):
    assert LineNumberMatcher(22)(TraceContext(frame, object(), object())) is False
