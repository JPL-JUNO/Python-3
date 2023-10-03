"""
@Title: 型变
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 22:07:51
@Description: 
"""

from collections.abc import Callable


def update(
    probe: Callable[[], float],
    display: Callable[[float], None]
) -> None:
    temperature = probe()
    display(temperature)


def probe_ok() -> int:
    return 42


def display_wrong(temperature: int) -> None:
    # display_wrong 不与 Callable[[float], None] 相容
    # 预期 int 参数的函数不一定能处理 float 值，比如说 hex 接受 int 值，但是 float 不能
    print(hex(temperature))


# mypy 会报错
update(probe_ok, display_wrong)  # type error


def display_ok(temperature: complex) -> None:
    # 接受 complex 值的函数也能处理 float 参数，因为 float 与 complex 相容
    print(temperature)

# int, float, complex 是没有名义上的子类型关系的
# 但是 PEP 484 声称，int 与 float 相容， float 与 complex 相容
# int 实现了 float 的所有操作，也额外实现了一些其他的操作，比如说按位运算


update(probe_ok, display_ok)
