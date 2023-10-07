"""
@Title: contextlib.contextmanager – Creating context managers
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 21:24:46
@Description: 
"""
import time
import datetime
import contextlib


# 创建一个函数表示内容激活了多久
@contextlib.contextmanager
def timer(name):
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    print("%s took %s" % (name, stop_time - start_time))


with timer("basic timer"):
    time.sleep(.1)


# 将标准的打印输出至文件中
@contextlib.contextmanager
def write_to_log(name):
    """可读性太差，需要改善，可以用装饰器，
    但是需要将输出转为宁一个的输入，也很麻烦"""
    with open(f'{name}.txt', 'w') as fh:
        with contextlib.redirect_stdout(fh):
            with timer(name):
                yield


@write_to_log('some_name')
def some_function():
    print("This will be written to 'some_name.txt'")


some_function()


@contextlib.contextmanager
def write_to_log(name):
    """That’s where the ExitStack context manager comes in. 
    It allows the easy combining of multiple context managers 
    without increasing the indentation level"""
    with contextlib.ExitStack() as stack:
        fh = stack.enter_context(open(f'{name}.txt', 'w'))
        stack.enter_context(contextlib.redirect_stdout(fh))
        stack.enter_context(timer(name))
        yield


@write_to_log('some_name')
def some_function():
    print("This will be written to 'some_name.txt' using ExitStack")


some_function()


# 手动处理
with contextlib.ExitStack() as stack:
    fh = stack.enter_context(open('file.txt', 'w'))
    new_stack = stack.pop_all()

bytes_written = fh.write('fh is still open')
new_stack.close()
try:
    fh.write('cant write anymore')
except ValueError as e:
    print(e)
