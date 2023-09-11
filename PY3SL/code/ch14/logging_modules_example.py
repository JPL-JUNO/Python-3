"""
@Title: 命名日志记录器实例 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 21:23:10
@Description: 
"""

import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger("package.module1")
logger2 = logging.getLogger("package.module2")

logger1.warning("This message comes from one module")
logger2.warning("This comes from another module")
