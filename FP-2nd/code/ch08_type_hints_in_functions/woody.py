"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 15:20:27
@Description: 
"""
from birds import *

woody = Bird()
# 这一行没有类型提示，mypy 没有检查
alert(woody)  # 但是运行报错，因为 Bird 根本没有实现 quack 方法
alert_duck(woody)
alert_bird(woody)
