#!/usr/bin/env python
#简单的星空实例，单击左键移动星空中心

import random, math, pygame
from pygame.locals import *

WINSIZE = [640, 480]     # 窗口大小
WINCENTER = [320, 240]   # 窗口中心
NUMSTARS = 150           # 星星的数量


def init_star():         # 创建新的星星
    dir = random.randrange(100000) # 随机生成一个数——角度
    velmult = random.random()*.6+.4  # 随机生成星星的总速度
    vel = [math.sin(dir) * velmult, math.cos(dir) * velmult] # 获得x,y方向的速度
    return vel, WINCENTER[:]   # 返回速度和中心


def initialize_stars():  # 创造一个新的星空
    stars = []   # 星星的列表
    for x in range(NUMSTARS):   # 循环生成星星
        star = init_star()     # 生成星星
        vel, pos = star       # 获取星星的速度与位置
        steps = random.randint(0, WINCENTER[0])  #随机生成一个数，用于更新位置和速度
        pos[0] = pos[0] + (vel[0] * steps)   # 为星星更细位置和速度
        pos[1] = pos[1] + (vel[1] * steps)
        vel[0] = vel[0] * (steps * .09)
        vel[1] = vel[1] * (steps * .09)
        stars.append(star)
    move_stars(stars)  # 移动星星
    return stars   # 返回星星的列表
  

def draw_stars(surface, stars, color): # 画星星的方法
    for vel, pos in stars:   # 遍历每个星星
        pos = (int(pos[0]), int(pos[1]))  # 获取其位置
        surface.set_at(pos, color)   # 设置每个星星的位置和颜色


def move_stars(stars): # 移动星星的方法
    for vel, pos in stars:
        pos[0] = pos[0] + vel[0]  #更新位置
        pos[1] = pos[1] + vel[1]
        if not 0 <= pos[0] <= WINSIZE[0] or not 0 <= pos[1] <= WINSIZE[1]: # 若出界
            vel[:], pos[:] = init_star() # 则重新生成
        else:
            vel[0] = vel[0] * 1.05  # 否则加速星星
            vel[1] = vel[1] * 1.05
  

def main():
    random.seed()   # 创建随机数的种子
    stars = initialize_stars()   # 初始化星星
    clock = pygame.time.Clock()  # 计时
    pygame.init()   # 初始化pygame
    screen = pygame.display.set_mode(WINSIZE) # 生成窗口
    pygame.display.set_caption('pygame Stars Example')  # 设置窗口的标题
    white = 255, 240, 200   # 设置白色white变量
    black = 20, 20, 40  # 设置黑色black变量
    screen.fill(black)  # 将窗口填充成black色

    done = 0
    while not done:
        draw_stars(screen, stars, black)   # 画星星
        move_stars(stars)  #移动星星
        draw_stars(screen, stars, white) #画星星
        pygame.display.update()  # 刷新屏幕
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                done = 1
                break
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                WINCENTER[:] = list(e.pos)
        clock.tick(50)


if __name__ == '__main__':
    main()   # 运行程序


