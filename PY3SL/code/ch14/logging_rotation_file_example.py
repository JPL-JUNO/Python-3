"""
@Title: 旋转日志文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 20:38:57
@Description: 
"""

import glob
import logging
import logging.handlers

# 始终保持最新的日志
LOG_FILENAME = "logging_rotation_file_example.out"

# 实例化一个处理对象
my_logger = logging.getLogger("MyLogger")
# 设置处理的等级
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    # 每次达到大小限制时，就会追加后缀 .1 进行重命名
    # 现有的各个备份文件也会被重命名，时后缀递增，并且 .5 文件会被删除
    backupCount=5,
)
my_logger.addHandler(handler)
# 为啥没有 MyLogger 的输出
for i in range(20):
    my_logger.debug("i = %d" % i)
log_files = glob.glob("%s*" % LOG_FILENAME)
for filename in log_files:
    print(filename)
