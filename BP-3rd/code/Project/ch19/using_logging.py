"""
@Title: 一个使用模块logging的程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 09:22:26
@Description: 
"""

import logging

# 记录不同类型的条目（信息、调试信息、警告、自定义类型等）
# 默认情况下，只记录警告

logging.basicConfig(level=logging.INFO, filename="running_log.log")
logging.info("Starting program")
logging.info("Trying to divide 1 by 0")
print(1 / 0)
logging.info("The division succeeded")
logging.info("Ending program")
