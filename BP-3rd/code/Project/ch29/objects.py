"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 10:43:08
@Description: 
"""

import pygame
import config
from random import randrange


class SquishSprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        # 矩形的方法inflate调整矩形的尺寸——在水平和垂直方向调整指定数量的像素。这个方
        # 法用于收缩香蕉的边界，从而在香蕉和铅锤重叠到一定程度后，才认为香蕉被砸到。
        self.area = screen.get_rect().inflate(shrink, shrink)


class Weight(SquishSprite):
    def __init__(self, speed):
        super().__init__(config.weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        """
        将铅锤移到屏幕顶端（使其刚好看不到），并放在一个随机的水平位置
        """
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 0

    def update(self):
        """
        根据铅锤的速度垂直向下移动相应的距离。同时，根据
        铅锤是否已到达屏幕底部相应地设置属性landed
        """
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom


class Banana(SquishSprite):
    def __init__(self):
        """
        绝望的香蕉。它使用SquishSprite的构造函数来设置香蕉图像，并停留
        在屏幕底部附近，且水平位置由鼠标的当前位置决定（有一定的限制）
        """
        super().__init__(config.banana_image)
        self.rect.bottom = self.area.bottom

        # 这些内边距表示图像中不属于香蕉的部分
        # 如果铅锤进入这些区域，并不认为它砸到了香蕉：
        self.pad_top = config.banana_pad_top
        self.pad_side = config.banana_pad_side

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    def touches(self, other):
        """
        判断香蕉是否与另一个精灵（如铅锤）发生了碰撞。这里没有直接
        使用矩形的方法colliderect，而是先使用矩形的方法inflat以及
        pad_side和pad_top计算出一个新的矩形，这个矩形不包含香蕉图
        像顶部和两边的“空白”区域
        """
        # 通过剔除内边距来计算bounds：
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        # 将 bounds 移动到与香蕉底部对齐
        bounds.bottom = self.rect.bottom
        # 检查bounds是否与另一个对象的rect重叠
        return bounds.colliderect(other.rect)
