import pygame
from math import *

img = pygame.image.load('graphics/d.bmp')  # 加载球的图片


class ball(object):  # 定义一个球的类（角色）
    def __init__(self, x0, y0, width, height, radius, number):  # 初始化球的属性
        self.__x0 = x0  # 设置球的坐标
        self.__y0 = y0
        self.__width = width  # 设置球的宽带
        self.__height = height  # 设置球的高度
        self.__radius = radius  # 设置球的半径
        self.number = number + 1  # 设置球的数量
        self.__angle = pi / 2  # 设置球的角度
        self.__caught = False  # 设置拿手的球 ("False" = Right)
        self.__x = x0 + (self.__radius * cos(self.__angle))  # 设置位置
        self.__y = y0 - (self.__radius * sin(self.__angle))
        self.visibility = False  # 设置是否可见

    def draw(self, win):  # 画球
        if self.visibility == True:  # 如果可见， 就画球
            self.move()  # 先移动
            win.blit(img, (self.__x, self.__y))  # 将球输出到窗口

    def move(self):  # 移动球功能
        # 从一个玩家的手开始以抛物线模式移动球
        # 并在另一个结束
        if self.__caught == False:
            self.__angle += pi / (24 * self.number)  # 抛物线运动
            self.__x = self.__x0 + (self.__radius * cos(self.__angle))
            self.__y = self.__y0 - (self.__radius * sin(self.__angle))
        else:
            self.__angle -= pi / (24 * self.number)
            self.__x = self.__x0 + (self.__radius * cos(self.__angle))
            self.__y = self.__y0 - (self.__radius * sin(self.__angle))

    def setCoord(self, x, y, angle):  # 用于设置球的坐标和角度的功能
        self.__x0 = x
        self.__y0 = y
        self.__angle = angle

    def getCoords(self):
        return (self.__x, self.__y, self.__angle)  # 检索球的坐标和角度的功能

    def caughtBall(self, c):  # 告诉哪个手抓球的功能
        self.__caught = c

    def getRadius(self):  # 获得球的半径的函数
        return self.__radius
