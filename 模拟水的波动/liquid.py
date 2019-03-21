#!/usr/bin/env python

"""照片模拟水的波动效果"""

import pygame, os
from pygame.locals import *
from math import sin  # 导入正弦函数的工具箱
import time

main_dir = os.path.split(os.path.abspath(__file__))[0]  # 获取当前文件所在路径

def main():
    pygame.init()  # 初始化
    screen = pygame.display.set_mode((640, 480), HWSURFACE|DOUBLEBUF)  # 生成一个窗口

    imagename = os.path.join(main_dir, 'data', 'liquid.bmp')  # 拼接图片路径
    bitmap = pygame.image.load(imagename)    # 加载图片
    bitmap = pygame.transform.scale2x(bitmap) # 将图像放大两倍
    bitmap = pygame.transform.scale2x(bitmap) # 将图像放大两倍

    if screen.get_bitsize() == 8: # 以相同的格式获取图像和屏幕
        screen.set_palette(bitmap.get_palette())
    else:
        bitmap = bitmap.convert()

    anim = 0.0

    while 1:
        for e in pygame.event.get():   # 处理事件
            if e.type in [QUIT, KEYDOWN, MOUSEBUTTONDOWN]:
                return

        anim = anim + 0.02
        for x in range(0,640,20):   # 模拟水的波动效果
            xpos = (x + (sin(anim + x * .01) * 15)) + 20
            for y in range(0, 480, 20):
                ypos = (y + (sin(anim + y * .01) * 15)) + 20
                screen.blit(bitmap, (x, y), (xpos, ypos, 20, 20))

        pygame.display.flip()  # 更新
        time.sleep(0.01)       # 等待0.01s


if __name__ == '__main__': 
    main()


