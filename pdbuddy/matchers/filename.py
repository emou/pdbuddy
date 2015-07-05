from __future__ import absolute_import

import re

from pdbuddy.matchers.base import BaseMatcher


class FilenameMatcher(BaseMatcher):
    """Matches the filename of the currently executed code object."""

    def __init__(self, filename_regex, firstlineno=None):
        self.filename_regex = re.compile(filename_regex)
        self.firstlineno = firstlineno

    def __call__(self, context):
        fname = context.definition_filename
        firstlineno = context.definition_line
        if not self._match_filename(fname):
            return False
        return self.firstlineno is None or firstlineno == self.firstlineno

    def _match_filename(self, fname):
        return self.filename_regex.match(fname)
