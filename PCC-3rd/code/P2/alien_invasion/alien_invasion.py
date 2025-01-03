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
from bullet import Bullet
from alien import Alien


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
        # 修改为全屏
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # 修改设置中的宽和高
        # 确保在可以使用 Q 退出的，全屏下是没有关闭窗口的
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width

        self.clock = pygame.time.Clock()

        # set the background color
        # self.bg_color = (230, 230, 230)
        # self.bg_color = self.settings.bg_color

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        # 用于管理（有效）子弹
        self.bullets = pygame.sprite.Group()

        # 外星人组
        self.aliens = pygame.sprite.Group()
        # 创建舰队
        self._create_fleet()

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
            # 更新子弹
            self._update_bullets()
            self._update_alien()
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
        # 新增子弹的开火键处理
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """ respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # the group automatically calls update() for each sprite in the group.
        # calls bullet.update() for each bullet we place in the group bullets.
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            # When you use a for loop with a list (or a group in Pygame), Python
            # expects that the list will stay the same length as long as the loop is running.
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self):
        # redraw the screen during each pass through the loop
        # self.screen.fill(self.bg_color)
        # 直接使用设置中的颜色参数
        self.screen.fill(self.settings.bg_color)
        # 把子弹画出来
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw the ship on the screen by calling ship.blitme
        self.ship.blitme()

        # When you call draw() on a group, Pygame draws each element in the
        # group at the position defined by its rect attribute. The draw() method
        # requires one argument: a surface on which to draw the elements from the
        # group.
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        # make an alien
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        # self.aliens.add(alien)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        # current_x = alien_width
        while current_y < (self.settings.screen_height - 2 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # finished a row; reset x value, and increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_alien(self):
        """update the positions of all aliens in the feet"""
        # Check if the fleet is at an edge, then update positions.
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """如果有任何一个外星人到达边缘，舰队改变方向"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """舰队下降并且改变运动方向"""
        # 舰队整体下降
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # 舰队方向改变
        self.settings.fleet_direction *= -1


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
