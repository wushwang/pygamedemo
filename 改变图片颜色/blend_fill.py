#!/usr/bin/env python
import os
import pygame
from pygame.locals import *

def usage ():  # 使用说明的方法
    print ("按R\G\B分别改变对应颜色的值")
    print ("1-9增加步长")
    print ("A - ADD, S- SUB, M- MULT, - MIN, + MAX")
    print ("空格改变模式")


main_dir = os.path.split(os.path.abspath(__file__))[0]  # 获取文件所在路径
data_dir = os.path.join(main_dir, 'data')  # 拼接上data文件夹

def main():
    color = [0, 0, 0]   # 定义颜色
    changed = False     # 是否改变
    blendtype = 0      # 混合类型
    step = 5           # 增加步长

    pygame.init ()  # 初始化
    screen = pygame.display.set_mode ((640, 480), 0, 32) # 生成窗口
    screen.fill ((100, 100, 100))  # 填充颜色

    image = pygame.image.load (os.path.join (data_dir, "liquid.bmp")).convert() # 加载图片
    blendimage = pygame.image.load (os.path.join (data_dir, "liquid.bmp")).convert() # 加载图片
    screen.blit (image, (10, 10)) # 输出图片
    screen.blit (blendimage, (200, 10)) #输出图片

    pygame.display.flip ()  # 更新
    pygame.key.set_repeat (500, 30) # 500ms后每隔30ms触发该事件一次
    usage()  # 输出说明书

    going = True
    while going:  # 进入死循环
        for event in pygame.event.get ():  # 处理循环事件
            if event.type == QUIT:  # 退出事件
                going = False

            if event.type == KEYDOWN: # 处理键被按下的事件
                usage ()

                if event.key == K_ESCAPE:  # 空格键事件
                    going = False  # 结束游戏

                if event.key == K_r:  # r键
                    color[0] += step  # 改变红色
                    if color[0] > 255: # 大于255时
                        color[0] = 0   # 设定为0
                    changed = True

                elif event.key == K_g:
                    color[1] += step
                    if color[1] > 255:
                        color[1] = 0
                    changed = True

                elif event.key == K_b:
                    color[2] += step
                    if color[2] > 255:
                        color[2] = 0
                    changed = True

                elif event.key == K_a:   # 设置混合类型，a键为加，s键为减
                    blendtype = BLEND_ADD
                    changed = True
                elif event.key == K_s:
                    blendtype = BLEND_SUB
                    changed = True
                elif event.key == K_m:
                    blendtype = BLEND_MULT
                    changed = True
                elif event.key == K_PLUS:
                    blendtype = BLEND_MAX
                    changed = True
                elif event.key == K_MINUS:
                    blendtype = BLEND_MIN
                    changed = True

                elif event.key in (K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9):  # 通过1-9，设定每次增加的幅度
                    step = int (event.unicode)

            if changed:  #如果有改变
                screen.fill ((100, 100, 100)) # 窗口填充颜色
                screen.blit (image, (10, 10)) # 加载图片
                blendimage.blit (image, (0, 0)) # 输出图片
                blendimage.fill (color, None, blendtype) # 给图片填充颜色
                screen.blit (blendimage, (200, 10))  # 输出图片
                print ("Color: %s, Pixel (0,0): %s" % (tuple(color), [blendimage.get_at ((0, 0))])) # 打印图片
                changed = False  # 将changed重新设置为False
                pygame.display.flip () # 刷新


    pygame.quit() # 退出游戏


if __name__ == '__main__': 
    main() # 程序入口
