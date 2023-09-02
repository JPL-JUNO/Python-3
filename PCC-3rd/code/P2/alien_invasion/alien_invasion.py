"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-02 20:11:13
@Description: 
"""

import sys
import pygame

# 可以统一修改参数设置
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""

        pygame.init()

        self.settings = Settings()

        # create a display window
        # self.screen = pygame.display.set_mode((1200, 800))
        # 在设置中统一使用参数
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        # set the background color
        # self.bg_color = (230, 230, 230)
        # self.bg_color = self.settings.bg_color

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            """Start the main loop for the game"""

            # 封装成函数
            self._check_events()
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            # 更新飞船的位置
            # 不是循环，一次也只移动一个 pixel
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """response to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 第二次重构，调用检查键盘按下的操作
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # 第二次重构，调用检查键盘抬起的操作
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to key press"""
        if event.key == pygame.K_RIGHT:
            # make the ship to the right
            # self.ship.rect.x += 1
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        # self.screen.fill(self.bg_color)
        # 直接使用设置中的颜色参数
        self.screen.fill(self.settings.bg_color)

        # draw the ship on the screen by calling ship.blitme
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
