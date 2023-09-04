python setup.py build

@REM Setuptools创建了一个名为build的目录，其中包含子目录lib。同时将将hello.py复制到了这个
@REM 子目录中。目录build相当于工作区，Setuptools在其中组装包（以及编译扩展库等）。安装时不需
@REM 要执行命令build，因为当你执行命令install时，如果需要，命令build会自动运行。

python setup.pt install

@REM 尝试安装这个模块


@REM 要创建源代码归档文件，可使用命令sdist（表示source distribution）
python setup.py sdist

@REM 如果只想就地编译扩展（在大多数UNIX系统中，这都将在当前目录中生成一个名为
@REM palindrome.so的文件），可使用如下命令：
python setup.py build_ext --inplace