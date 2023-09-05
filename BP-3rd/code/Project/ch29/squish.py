# """
# @Title: 游戏主模块
# @Author(s): Stephen CUI
# @LastEditor(s): Stephen CUI
# @CreatedTime: 2023-09-05 11:36:38
# @Description: 这个模块包含游戏 Squish 的主游戏逻辑
# """

import os
import sys
import pygame
from pygame.locals import *
import objects
import config


class State:
    """

    """

    def handle(self, event):
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def first_display(self, screen):
        """
        """
        screen.fill(config.background_color)
        pygame.display.flip()

    def display(self, screen):
        """
        在后续显示状态时使用，其默认行为是什么都不做
        交给子类去实现具体的功能
        """
        pass


class Level(State):
    """
    游戏关卡。它计算落下了多少个铅锤，移动精灵并执行其他与游戏逻辑相关的任务
    """

    def __init__(self, number=1) -> None:
        self.number = number
        # 还需躲开多少个铅锤才能通过当前关卡？
        self.remaining = config.weights_per_level

        speed = config.drop_speed
        # 每过一关都将速度提高 speed_increase：
        speed += (self.number - 1) * config.speed_increase
        # 创建铅锤和香蕉：
        self.weight = objects.Weight(speed)
        self.banana = objects.Banana()
        both = self.weight, self.banana
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        self.sprites.update()

        if self.banana.touches(self.weight):
            game.next_state = GameOver()

        elif self.weight.landed:
            self.weight.reset()
            self.remaining -= 1
            if self.remaining == 0:
                game.nex_state = LevelCleared(self.number)

    def display(self, screen):
        """
        在第一次显示（清屏）后显示状态。不同于firstDisplay，
        这个方法调用pygame.display.update并向它传递一个需要
        更新的矩形列表，这个列表是由self.sprites.draw提供的
        """
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)


class Paused(State):
    finished = 0
    image = None
    text = ""

    def handle(self, event):
        """
        这样来处理事件：将这项任务委托给State（它只处理退出事件），
        并对按键和鼠标单击做出响应。如果用户按下了键盘键或单击了鼠标，
        就将 self.finished 设置为 True
        """
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        if self.finished:
            game.next_state = self.next_state()

    def first_display(self, screen):
        """
        在首次显示暂停状态时调用，它绘制图像（如果指定了）并渲染文本
        """
        # 首先，通过使用背景色填充屏幕来清屏：
        screen.fill(config.background_color)

        # 创建一个使用默认外观和指定字号的Font对象：
        font = pygame.font.Font(None, config.font_size)

        # 获取self.text中的文本行，但忽略开头和末尾的空行：
        lines = self.text.strip().splitlines()
        # 使用 font.get_linesize() 获取每行文本的高度，并计算文本的总高度：
        height = len(lines) * font.get_linesize()

        center, top = screen.get_rect().center
        top -= height // 2
        # 如果有图像要显示：
        if self.image:
            # 加载该图像
            image = pygame.image.load(self.image).convert()
            # 获取其rect：
            r = image.get_rect()
            # 将文本下移图像高度一半的距离
            top += r.height // 2
            # 将图像放在文本上方 20 像素处：
            r.midbottom = center, top - 20
            # 将图像传输到屏幕上：
            screen.blit(image, r)

        antialias = 1  # 消除文本的锯齿
        black = 0, 0, 0  # 使用黑色渲染文本

        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()
        # 显示所做的所有修改：
        pygame.display.flip()


class Info(Paused):
    """
    显示一些游戏信息的简单暂停状态，紧跟在这个状态后面的是Level状态（第一关）
    """
    next_state = Level
    text = """
    In this game you are a banana,
    trying to survive a course in
    self-defense against fruit, where the
    participants will 'defend' themselves
    against you with a 16 ton weight.
    """


class StartUp(Paused):
    """
    显示启动图像和欢迎消息的暂停状态，紧跟在它后面的是Info状态
    """
    next_state = Info
    image = config.splash_image
    text = '''
    Welcome to Squish,
    the game of Fruit Self-Defense
    '''


class LevelCleared(Paused):
    """
    指出用户已过关的暂停状态，紧跟在它后面的是表示下一关的Level状态
    """

    def __init__(self, number) -> None:
        self.number = number
        self.text = """
        Level {} cleared
        Click to start next level
        """.format(self.number)

    def next_state(self):
        return Level(self.number + 1)


class GameOver(Paused):
    """
    指出游戏已结束的状态，紧跟在它后面的是表示第一关的 Level 状态
    """
    next_state = Level
    text = """
    Game Over
    Click to Restart, Esc to Quit
    """


class Game:
    """
    负责主事件循环（包括在不同游戏状态之间切换）的游戏对象
    """

    def __init__(self, *args):
        # 获取游戏和图像所在的目录：
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        # 切换到这个目录，以便之后能够打开图像文件：
        os.chdir(dir)

        # 最初不处于任何状态：
        self.state = None
        self.clock = pygame.time.Clock()

        # 在第一次事件循环迭代中切换到StartUp状态：
        self.next_state = StartUp()

    def run(self):
        # 初始化所有的Pygame模块
        pygame.init()

        # 决定在窗口还是整个屏幕中显示游戏：
        flag = 0  # 默认在窗口中显示游戏
        if config.full_screen:
            flag = FULLSCREEN  # 全屏模式
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption("Fruit Self Defense")
        pygame.mouse.set_visible(False)

        # 主循环
        while True:
            # (1)如果nextState被修改，就切换到修改后的状态并显示它（首次）：
            if self.state != self.next_state:
                self.state = self.next_state
                self.state.first_display(screen)
            # (2)将事件处理工作委托给当前状态：
            for event in pygame.event.get():
                self.state.handle(event)
            # (3)更新当前状态：
            self.state.update(self)
            # (4)显示当前状态：
            self.state.display(screen)
            # self.clock.tick(900)


if __name__ == "__main__":
    game = Game(*sys.argv)
    game.run()
