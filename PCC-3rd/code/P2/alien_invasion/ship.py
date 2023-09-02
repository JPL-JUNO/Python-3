"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-02 20:46:43
@Description: 
"""
import pygame


class Ship:
    def __init__(self, ai_game):
        """Initialize the ship ans set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load the ship image and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store a float for the ship's exact horizontal position
        self.x = float(self.rect.x)

        # Movement flag: start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the ship's position based on the movement flag."""
        # 增加对移动范围的限制，不能超出屏幕右侧
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # update the ship's x value, not the rect.
            self.x += self.settings.ship_speed
            # self.rect.x += 1
        # 不能超出屏幕左侧
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # self.rect.x -= 1
        self.rect.x = self.x
