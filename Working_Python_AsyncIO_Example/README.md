# AsyncIO Working Example
A straightforward example of how Python AsyncIO works

Python AsyncIO is based on coroutines. A coroutine is an asynchronous function
which can keep on executing without blocking other routines from execution.
Several coroutines can be in execution simultaneosly.

Awaiting a coroutine using <await> causes subsequent lines of code to be blocked
from execution till the result of the wait is reached. For this reason, a coroutine
which shouldn't block normal execution should be created as a scheduled <task>.
After a task is created, it should be awaited at the end of the "main" async
function to ensure that the async loop does not quit until the task is completed.

NOTE that an <await> statement does not block subsequent <await> statements.
Therefore if line 13 has <await coroutine1> and line 14 has <await coroutine2>,
coroutine2 will be set on await just as instantaneosly as coroutine1.

The example here makes use of two coroutines of different speeds of completion
in order to fully illustrate the point.
