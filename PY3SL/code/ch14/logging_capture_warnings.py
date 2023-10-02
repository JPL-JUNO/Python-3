"""
@Title: 与 warnings 模块集成
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 21:34:17
@Description: 
"""

import logging
import warnings
# 设置日志的等级
logging.basicConfig(level=logging.INFO)

warnings.warn("This warning is not sent to the logs")
logging.captureWarnings(True)

# 这个警告消息使用 WARNING 级别被发送到一个名为 py.warnings 的日志记录器
warnings.warn("This warning is sent to the logs")
