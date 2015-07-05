from __future__ import absolute_import

import pytest

from mock import Mock
from pdbuddy.matchers.filename import FilenameMatcher
from pdbuddy.trace_context import TraceContext


@pytest.fixture
def frame():
    frame = Mock()
    f_code = Mock()
    f_code.co_filename = 'foo.py'
    f_code.co_firstlineno = 23
    frame.f_code = f_code
    return frame


def test_star_matches_filename(frame):
    assert FilenameMatcher(r'.*')(TraceContext(frame, object(), object())) is True


def test_filename_filename(frame):
    assert FilenameMatcher(r'foo.py')(TraceContext(frame, object(), object())) is True


def test_not_matches_filename(frame):
    assert FilenameMatcher(r'xyz')(TraceContext(frame, object(), object())) is False
