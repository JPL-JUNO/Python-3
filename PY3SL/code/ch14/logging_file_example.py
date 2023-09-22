"""
@Title: 计入文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 20:08:35
@Description: 
"""

import logging

LOG_FILENAME = "logging_example.out"
# basicConfig() 函数建立默认处理器，将调试消息写至一个文件
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug("This message should go to the log file")
# 默认会追加进文件
# logging.debug("This another message")
with open(LOG_FILENAME, "rt") as f:
    body = f.read()

print("FILE:")
print(body)
