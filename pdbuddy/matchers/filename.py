from __future__ import absolute_import

import re

from pdbuddy.matchers.base import BaseMatcher


class FilenameMatcher(BaseMatcher):
    """Matches the filename of the currently executed code object."""

    def __init__(self, filename_regex, firstlineno=None):
        self.filename_regex = re.compile(filename_regex)
        self.firstlineno = firstlineno

    def match(self, frame, event, arg):
        if event != 'call':
            return

        f_code = frame.f_code
        fname = f_code.co_filename
        firstlineno = f_code.co_firstlineno
        if not self._match_filename(fname):
            return False
        return firstlineno is None or firstlineno == self.firstlineno

    def _match_filename(self, fname):
        return self.filename_regex.match(fname)
