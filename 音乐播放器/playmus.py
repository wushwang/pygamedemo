#!/usr/bin/env python

'''简单的音乐播放器'''
from __future__ import print_function
import pygame
import pygame.freetype
from pygame.locals import *
import sys
import os

class Window(object):
    instance = None

    def __new__(cls, *args, **kwds):
        if Window.instance is not None:
            return Window.instance
        self = object.__new__(cls)
        pygame.display.init()  # 初始化
        self.screen = pygame.display.set_mode((600, 400)) # 生成一个窗口
        Window.instance = self 
        return self

    def __init__(self, title):
        pygame.display.set_caption(title)  # 设置标题
        self.screen.fill(Color('white'))   # 填充背景色
        pygame.display.flip()   # 刷新

        pygame.freetype.init() 
        self.font = pygame.freetype.Font(None, 20)
        self.font.origin = True
        self.ascender = int(self.font.get_sized_ascender() * 1.5)
        self.descender = int(self.font.get_sized_descender() * 1.5)
        self.line_height = self.ascender - self.descender

        self.write_lines("'q', ESCAPE or close this window to quit\n"
                         "SPACE to play/pause\n"
                         "'r' to rewind\n"
                         "'f' to faid out over 5 seconds\n", 0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def close(self):  # 关闭方法
        pygame.display.quit()
        Window.instance = None

    def write_lines(self, text, line=0):  # 输出内容的方法
        w, h = self.screen.get_size()
        line_height = self.line_height
        nlines = h // line_height
        if line < 0:
            line = nlines + line
        for i, text_line in enumerate(text.split('\n'), line):
            y = i * line_height + self.ascender
            self.screen.fill(Color('white'), (0, i * line_height, w, line_height))
            self.font.render_to(self.screen, (15, y), text_line, Color('blue'))
        pygame.display.flip()


def main(file_path):  # 主函数
    with Window(file_path) as win:   
        win.write_lines('Loading ...', -1)   # 输出到行
        pygame.mixer.init(frequency=44100)   # 初始化声道
        try:
            paused = False  # 控制播放与暂停
            pygame.mixer.music.load(file_path)  # 加载音乐
            pygame.time.set_timer(USEREVENT, 500)  # 确保事件循环至少5秒一次
            pygame.mixer.music.play()    # 播放音乐
            win.write_lines("Playing ...\n", -1)

            while pygame.mixer.music.get_busy(): # 只要事件播放
                e = pygame.event.wait()   #获取事件
                if e.type == pygame.KEYDOWN: # 若事件为按下
                    key = e.key  # 获取按下的键
                    if key == K_SPACE:   # 若为空格键
                        if paused:  # 若paused为True
                            pygame.mixer.music.unpause() # 恢复音乐播放
                            paused = False #
                            win.write_lines("Playing ...\n", -1)
                        else:  # 若pause为false
                            pygame.mixer.music.pause() # 则暂停音乐播放
                            paused = True
                            win.write_lines("Paused ...\n", -1)
                    elif key == K_r:
                        pygame.mixer.music.rewind()  # 重新开始播放
                        if paused:
                            win.write_lines("Rewound.", -1)
                    elif key == K_f:
                        win.write_lines("Faiding out ...\n", -1)
                        pygame.mixer.music.fadeout(5000)  # 淡出的效果结束音乐播放
 
                    elif key in [K_q, K_ESCAPE]:
                        pygame.mixer.music.stop() # 停止播放
                       
                elif e.type == QUIT:  
                    pygame.mixer.music.stop()
                    
            pygame.time.set_timer(USEREVENT, 0)
        finally:
            pygame.mixer.quit()

if __name__ == '__main__':
    main('house_lo.mp3')


