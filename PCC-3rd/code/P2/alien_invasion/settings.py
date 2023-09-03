"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-02 20:34:47
@Description: 
"""


class Settings:
    def __init__(self,):
        """初始化游戏的设置"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship setting
        self.ship_speed = 1.5

        # bullet setting
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 对子弹的个数进行限制
        self.bullets_allowed = 3

        # Alien setting
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
