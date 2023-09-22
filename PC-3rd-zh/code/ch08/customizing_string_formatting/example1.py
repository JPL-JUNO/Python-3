"""
@Title: 自定义字符串的输出格式
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 10:51:40
@Description: 通过 format()函数和字符串方法来支持自定义的输出格式
"""

_format = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}/{d.day}/{d.year}",
    "dmy": "{d.day}/{d.month}/{d.year}",
}


class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code: str) -> str:
        if code == "":
            code = "ymd"
        fmt = _format[code]
        return fmt.format(d=self)
