from __future__ import absolute_import

from pdbuddy.formatters.base import BaseFormatter


class SimpleFormatter(BaseFormatter):

    def __call__(self, frame, event, arg):
        return str(frame.f_code)
