#!/usr/bin/env python

"""该代码演示了计时器"""


import os, pygame
from pygame.locals import *

try:
    from numpy import *
    from numpy.random import *
except ImportError:
    raise SystemExit('This example requires numpy and the pygame surfarray module')

pygame.surfarray.use_arraytype('numpy')

timer = 0  # 定义一个计时器变量

def stopwatch(message = None): 
    global timer   # 将timer变成全局变量
    if not message:  # 判断是否有消息
        timer = pygame.time.get_ticks()  # 获取时间点
        return  # 返回
    now = pygame.time.get_ticks() # 获取此时的时间点
    runtime = (now - timer)/1000.0 + .001    # 计算运行时间
    print ("%s %s %s" %  (message, runtime, ('seconds\t(%.2ffps)'%(1.0/runtime))))  # 输出消息运行时间
    timer = now  #将现在时间赋给计时器，用于下次计算



def VertGradientColumn(surf, topcolor, bottomcolor): # 创建一个新的3D垂直渐变数组
    topcolor = array(topcolor, copy=0)
    bottomcolor = array(bottomcolor, copy=0)
    diff = bottomcolor - topcolor
    width, height = surf.get_size()
    column = arange(height, dtype='float')/height  # 创建从0.0到1.0三元组的数组
    print('变换前：')
    print(column)
    column = repeat(column[:, newaxis], [3], 1)  
    print('变换后：')
    print(column)
    column = topcolor + (diff * column).astype('int') # 创建一个渐变列
    column = column.astype('uint8')[newaxis,:,:] #通过添加X使列成为3d图像列
    return pygame.surfarray.map_array(surf, column)  #3维数组转换成二维数组



def DisplayGradient(surf):  # 选择随机颜色并显示
    stopwatch()
    colors = randint(0, 255, (2, 3))  # 随机产生两个颜色数组
    column = VertGradientColumn(surf, colors[0], colors[1])  # 产生渐变色颜色素组
    pygame.surfarray.blit_array(surf, column)  # 将颜色数组输出到窗口
    pygame.display.flip()  # 更新屏幕
    stopwatch('Gradient:')



def main():  # 程序运行入口
    pygame.init()    # 初始化pygame
    pygame.mixer.quit()    # 初始化声音
    size = 600, 400  # 设置窗口大小
    os.environ['SDL_VIDEO_CENTERED'] = '1'   # 使窗口居中
    screen = pygame.display.set_mode(size, NOFRAME, 0)   # 生成窗口

    pygame.event.set_blocked(MOUSEMOTION) # 保持队列干净
    pygame.time.set_timer(USEREVENT, 500) # 设置定时器

    while 1:
        event = pygame.event.wait()   # 获取事件
        if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):   # 判断事件类型
            break      # 结束程序
        elif event.type == USEREVENT:   # 到达指定时间
            DisplayGradient(screen)     # 切换屏幕



if __name__ == '__main__': 
    main()  # 运行程序
