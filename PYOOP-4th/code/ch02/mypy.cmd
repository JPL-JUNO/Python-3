mypy --strict bad_hints.py
@REM bad_hints.py:14: error: Function is missing a return type annotation  [no-untyped-def]
@REM bad_hints.py:14: note: Use "-> None" if function does not return a value
@REM bad_hints.py:15: error: Argument 1 to "odd" has incompatible type "str"; expected "int"  [arg-type]
@REM bad_hints.py:19: error: Call to untyped function "main" in typed context  [no-untyped-call]
@REM Found 3 errors in 1 file (checked 1 source file)