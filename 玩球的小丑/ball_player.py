import pygame

# 加载图片
img = [pygame.image.load('graphics/a.bmp'),
       pygame.image.load('graphics/c.bmp'),
       pygame.image.load('graphics/e.bmp')]


# 头类
class player(object):
    def __init__(self, x, y, width, height):  # 初始化玩家大小和位置
        self.x = x  # 设置头的位置
        self.y = y
        self.__width = width  # 设置头的宽
        self.__height = height  # 设置头的高

    def draw(self, win):  # 我们绘制玩家的功能
        win.blit(img[1], (self.x, self.y), special_flags=3)  # 画出玩家头


# 胳膊类
class arm(object):
    def __init__(self, coords):  # 初始化玩家大小和位置
        self.__coords = coords

    def draw(self, win):  # 绘制手臂的功能
        pygame.draw.lines(win, (0, 0, 0), False, self.__coords, 10)  # 画臂

    def getCoords(self):  # 获取手臂坐标列表的功能
        return self.__coords


# 手类
class hand(object):
    def __init__(self, x, y, width, height, side):  # 初始化玩家大小和位置
        self.x = x
        self.y = y
        self.__width = width
        self.__height = height
        self.__side = side

    def draw(self, win):  # 画手的功能
        if self.__side:
            win.blit(img[2], (self.x, self.y), special_flags=3)
        else:
            win.blit(img[0], (self.x, self.y), special_flags=3)
