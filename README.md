# Uncommon Python Bug: ZeroDivisionError
This repository demonstrates a common yet easily overlooked error in Python: the `ZeroDivisionError`. While this error is typically straightforward, it can sometimes manifest in less obvious ways, especially within complex functions or unexpected code flows.

## Bug Description
The `bug.py` file shows a simple function where a division by zero might occur if the input `b` is 0.  This error can be challenging to debug when nested within larger programs or when the zero division condition isn't immediately apparent.

## Bug Solution
The `bugSolution.py` demonstrates ways to handle this exception: using `try-except` blocks for graceful error handling or adding input validation to prevent the error from occurring in the first place.  This also includes error messages to guide users when the exception happens.