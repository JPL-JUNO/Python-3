@REM 输入是一个模块名以及输入模块中的可选参数
python -m inspect -d example

python -m inspect -d example:A

@REM 如果使用 --details 参数，则会打印元数据而不是源代码
python -m inspect example:A.get_name