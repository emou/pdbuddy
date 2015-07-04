- Use issue tracker instead of this file

- Tests

- Higher-level interface instead of the OO matchers/processors/etc.
  * some form of concise DSL
  * maybe config file

- More matchers
  * line number matcher
  * method name matcher
  * class matcher
  * module matcher
  * thread matcher
  * global variable value
  * local variable name/value
  * caller matchers - apply some of the matchers (filename, module, method, etc.) to any level of
    the stack frame (parent frame is a good start). For example, something like "trace all calls to
    json.load that originate from module XYZ".

- More formatters:
  * function name
  * function arguments
  * line number
  * local/global variable names
  * stacktrace (support for limiting/filtering the stacktrace)
  * json/csv/etc. for post-processing

- Combining (concatenating, listing) formatters - any combination (concatenation, list, etc) of
  filename, filenumber, function name, class name, etc.

- More events (only `call` is supported currently)

- Watch attribute access (both get and set).

- Boolean operations between matchers (`and`, `not`, `or`, etc).

- Proper breakpoint support:
    * Actually support multiple breaks -- currently the debugger hijacks our tracer after the
      first breakpoint.
    * Investigate `pdb.Pdb`'s `set_break` method.

- pypi/distribute

- sampling matchers support - assign a probability to each matcher to, or configure it to only
  print once, twice, etc. in order to avoid cluttering the output.

- use decorators instead of hooks or `sys.settrace`, i.e. decorator for conditional breakpoint:

    ```python
    @pdbuddy.break_when(ArugmentMatcher('a', 42) or ModuleMatcher('some_module', target_frame=TargetFrame.parent))
    def foo(a):
       pass
   ```

   This would then break when `foo` is called directly from the `some_module` module.

- random wild ideas using library-specific hooks instead of `sys.settrace` that can be also used in
  production environment for logging:
  * sqlalchemy, django ORM, etc. matchers for SQL query matching some condition (accessed table,
    type of sql statement, etc.)
  * various http frameworks
  * unhandled exceptions (some of the networking errors in Python suck: log missing port/host
    information for errors like "Connection refused")

Of course, all that with a much prettier interface/DSL!
