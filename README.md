# pdbuddy: your Python debugging buddy

`pdbuddy` is a debugging tool that lets you trace function calls you are interested in.

It is generally a wrapper around `sys.settrace` that makes it easy to trace certain things you are
interested in.

It lets you define debugging behaviour in one place, so you don't have to edit system libraries, or
your code, adding debugging print statements, putting breakpoints and writing if-statements when
you want them to be conditional.

The tracing infrastructure supports various formatting of the traced calls, as well as filtering
the lines you are interested through matchers.

The breakpoint support is rudimental and only supports one breakpoint as the debugger hijacks our
tracing callback. Full support is being researched and planned for implementation.

# Example usage

## Tracing

The following code will output all function calls to functions defined in files with filename
matching the pattern `.*json.*`.

```python
import json

from pdbuddy import Tracer
from pdbuddy.formatters import SimpleFormatter
from pdbuddy.processors import TraceProcessor
from pdbuddy.matchers import CallMatcher, FilenameMatcher


def foo():
    return json.loads('{}')

Tracer([
    TraceProcessor(CallMatcher() & FilenameMatcher('.*json.*'),
                   SimpleFormatter())
]).install()

foo()
```

The output of the above program will be similar to this:

```
  <code object loads at 0x1018892b0, file "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.py", line 293>
  <code object decode at 0x1018a68b0, file "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/decoder.py", line 360>
  <code object raw_decode at 0x1018a69b0, file "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/decoder.py", line 371>
```

## Breakpoints (experimental)

This is very rudimentary and only supports setting one breakpoint as the debugger hijacks our
tracing function. A more complete implementation is planned.

The following code will set a breakpoint the first time a function defined on line 293 in a file
matching `.*json.*` is called.

```python
import json

from pdbuddy import Tracer
from pdbuddy.processors import BreakpointProcessor
from pdbuddy.matchers import CallMatcher, FilenameMatcher


def foo():
    json.loads('{}')

Tracer([
  BreakpointProcessor(CallMatcher() & FilenameMatcher('.*json.*', 293))
]).install()

foo()
```

# Running the tests

```bash
$ source env/bin/activate
$ ./bootstrap-tests.sh
```

Run the tests:

```
$ py.test tests
```

Make sure you're running `env/bin/py.test`.

```
$ which py.test
```

# TODO

Random items in [TODO.md](TODO.md).
