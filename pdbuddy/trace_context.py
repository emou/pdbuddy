class TraceContext(object):
    """A class representing the trace context.

    It is basically a wrapper around the frame, event and arg arguments pass to tracing functions
    that provides more convinient ways to extract data.
    """

    def __init__(self, frame, event, arg):
        self._frame = frame
        self._event = event
        self._arg = arg

    @property
    def name(self):
        return self._frame.f_code.co_name

    @property
    def definition_filename(self):
        """The filename of the file where the current code object was defined."""
        return self._frame.f_code.co_filename

    @property
    def definition_line(self):
        """The line in the file where the current code object was defined."""
        return self._frame.f_code.co_firstlineno

    @property
    def current_line(self):
        """The line number in the file that is currently being executed."""
        return self._frame.f_lineno

    def has_local_variable(self, variable_name):
        return variable_name in self._frame.f_locals

    def get_local_variable(self, variable_name):
        return self._frame.f_locals[variable_name]

    def is_call(self):
        return self._event == 'call'
