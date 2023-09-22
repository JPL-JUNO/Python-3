"""
@Title: 一个使用ConfigParser的程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 09:14:04
@Description: 
"""


from configparser import ConfigParser

CONFIG_FILE = "area.ini"
config = ConfigParser()
# 读取配置文件
config.read(CONFIG_FILE)

# 打印默认问候语（greeting）：
# 在messages部分查找问候语：
print(config["messages"].get("greeting"))

# 使用配置文件中的提示（question）让用户输入半径：
radius = float(input(config["messages"].get("question") + " "))

# 打印配置文件中的结果消息（result_message）；
# 以空格结束以便接着在当前行打印：
print(config["messages"].get("result_message"), end=" ")

# getfloat()将获取的值转换为浮点数：
print(config["numbers"].getfloat("pi") * radius ** 2)
