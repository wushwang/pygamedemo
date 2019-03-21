#!/usr/bin/env python

"""加载字体文件"""

import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_
import sys
import locale


def main():
    pygame.init()  # 初始化pygame工具箱
    size = 400, 200  # 设置窗口的大小
    screen = pygame.display.set_mode(size)  # 生成一个窗口

    fg = 250, 240, 230  # 前景色
    bg = 5, 5, 5   # 背景色
    wincolor = 40, 40, 90 # 窗口的颜色
    screen.fill(wincolor)  #填充颜色

    font = pygame.font.Font(None, 80)  # 加载字体，大小为80
    text = 'Fonty'  # 要现实的文本
    size = font.size(text) # 字体的大小

    ren = font.render(text, 0, fg, bg)  # 渲染字体
    screen.blit(ren, (10, 10))  # 输出字体

    font.set_underline(1) # 设置下划线
    ren = font.render(text, 0, fg) # 渲染字体
    screen.blit(ren, (10, 40 + size[1])) # 输出字体
    font.set_underline(0) # 取消下划线


    a_sys_font = pygame.font.SysFont("Arial", 60) # 加载系统字体

    a_sys_font.set_bold(1)  # 加粗字体
    ren = a_sys_font.render(text, 1, fg, bg)  # 渲染字体
    screen.blit(ren, (30 + size[0], 10)) # 输出字体
    a_sys_font.set_bold(0) # 取消字体

    a_sys_font.set_italic(1)  # 设置斜体
    ren = a_sys_font.render(text, 1, fg)  # 渲染字体
    screen.blit(ren, (30 + size[0], 40 + size[1]))  # 输出字体
    a_sys_font.set_italic(0)  # 取消斜体

    pygame.display.flip()  # 更新屏幕
    while 1:   
        if pygame.event.wait().type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            break

if __name__ == '__main__': 
    main()
    
