# Foundation Acceptance Tests

## AT-001 — Runtime identity
The service reports **CPython 3.14.6**.

## AT-002 — Simple execution
```python
print("Hello from WebPython")
```
Expected stdout: `Hello from WebPython` and exit code `0`.

## AT-003 — Standard library
```python
import math
print(math.sqrt(144))
```
Expected stdout: `12.0`.

## AT-004 — Build validation
Invalid Python fails BUILD before execution.

## AT-005 — Runtime error
A Python exception is returned through stderr with a non-zero exit code.

## AT-006 — Timeout
An infinite loop cannot run indefinitely.

## AT-007 — Wrong runtime protection
If the configured interpreter is not CPython 3.14.6, execution is rejected.

## AT-008 — Project boundary
A filename cannot escape its project workspace using path traversal.