@REM 输出当前活动代码页
chcp

@REM 执行 python 文件
python default_encoding.py

@REM  locale.getpreferredencoding() -> 'cp936' # 最重要的设置
@REM                  type(my_file) -> <class '_io.TextIOWrapper'>
@REM               my_file.encoding -> 'cp936'
@REM            sys.stdout.isatty() -> True # 结果输出到控制台，因此返回 True
@REM            sys.stdout.encoding -> 'utf-8'
@REM             sys.stdin.isatty() -> True
@REM             sys.stdin.encoding -> 'utf-8'
@REM            sys.stderr.isatty() -> True
@REM            sys.stderr.encoding -> 'utf-8'
@REM       sys.getdefaultencoding() -> 'utf-8'
@REM    sys.getfilesystemencoding() -> 'utf-8'

@REM sys.stdout.isatty() 的输出将变为 False
python default_encodings.py > encoding.log