from __future__ import absolute_import

import sys

from pdbuddy.printers import StdoutPrinter


class Tracer(object):

    def __init__(self, processors, printer=None):
        """Initialize a Tracer object.

        :param processors: A list of processors to apply on each trace.
        :param printer: Specify the printer used to output the trace result. If ommited, defaults
        to ``pdbuddy.printers.StdoutPrinter``.
        """
        self.processors = processors
        if printer is None:
            printer = StdoutPrinter()
        self.printer = printer

    def install(self):
        """Install the grepper as the tracing function of the process."""
        sys.settrace(self)

    def __call__(self, frame, event, arg):
        """Perform the actual call tracing."""
        for processor in self.processors:
            result = processor(frame, event, arg)
            if result is not None:
                self.printer(result)
