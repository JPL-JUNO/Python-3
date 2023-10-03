mypy messages.py

@REM The command-line option --disallow-untyped-defs makes Mypy flag any function
@REM definition that does not have type hints for all its parameters and for its return value.
mypy --disallow-untyped-defs messages_test.py

@REM 不完整的类型提示将报错，全写或全不写不会报错
mypy --disallow-incomplete-defs messages_test.py