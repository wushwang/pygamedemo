#!/usr/bin/env python
import sys
import os

import pygame
from pygame.transform import scale
from pygame.locals import *

main_dir = os.path.dirname(os.path.abspath(__file__))  # 获取文件的路径
zoom_factor = 8 # 放大倍数

def draw_arrow(surf, color, posn, direction): # 画箭头
    x, y = posn
    if direction == 1:   # 上箭头
        pointlist = ((x - 29, y + 30), (x + 30, y + 30), (x + 1, y - 29), (x, y - 29))
    elif direction == 2: # 下箭头
        pointlist = ((x - 29, y - 29), (x + 30, y - 29), (x + 1, y + 30), (x, y + 30))
    elif direction == 3: # 左箭头
        pointlist = ((x + 30, y - 29), (x + 30, y + 30), (x - 29, y + 1), (x - 29, y))
    else:  # 右箭头
        pointlist = ((x - 29, y - 29), (x - 29, y + 30), (x + 30, y + 1), (x + 30, y))
    pygame.draw.polygon(surf, color, pointlist)  # 绘制相应箭头

def add_arrow_button(screen, regions, posn, direction):  # 绘制箭头按钮
    draw_arrow(screen, Color('black'), posn, direction)  # 调用画箭头的方法
    draw_arrow(regions, (direction, 0, 0), posn, direction) # 画按钮的区域

def scroll_view(screen, image, direction, view_rect):  # 滚动图片
    dx = dy = 0
    src_rect = None
    zoom_view_rect = screen.get_clip()
    image_w, image_h = image.get_size()
    if direction == 1:
        if view_rect.top > 0:
            screen.scroll(dy=zoom_factor)
            view_rect.move_ip(0, -1)
            src_rect = view_rect.copy()
            src_rect.h = 1
            dst_rect = zoom_view_rect.copy()
            dst_rect.h = zoom_factor
    elif direction == 2:
        if view_rect.bottom < image_h:
            screen.scroll(dy=-zoom_factor)
            view_rect.move_ip(0, 1)
            src_rect = view_rect.copy()
            src_rect.h = 1
            src_rect.bottom = view_rect.bottom
            dst_rect = zoom_view_rect.copy()
            dst_rect.h = zoom_factor
            dst_rect.bottom = zoom_view_rect.bottom
    elif direction == 3:
        if view_rect.left > 0:
            screen.scroll(dx=zoom_factor)
            view_rect.move_ip(-1, 0)
            src_rect = view_rect.copy()
            src_rect.w = 1
            dst_rect = zoom_view_rect.copy()
            dst_rect.w = zoom_factor
    elif direction == 4:
        if view_rect.right < image_w:
            screen.scroll(dx=-zoom_factor)
            view_rect.move_ip(1, 0)
            src_rect = view_rect.copy()
            src_rect.w = 1
            src_rect.right = view_rect.right
            dst_rect = zoom_view_rect.copy()
            dst_rect.w = zoom_factor
            dst_rect.right = zoom_view_rect.right
    if src_rect is not None:
        scale(image.subsurface(src_rect), dst_rect.size, screen.subsurface(dst_rect))
        pygame.display.update(zoom_view_rect)

def main(image_file=None):
    if image_file is None:  # 若文件不存在
        image_file = os.path.join(main_dir, 'data', 'arraydemo.bmp')  # 加载该文件
    margin = 80
    view_size = (30, 20)
    zoom_view_size = (view_size[0] * zoom_factor, view_size[1] * zoom_factor)
    win_size = (zoom_view_size[0] + 2 * margin, zoom_view_size[1] + 2 * margin)
    background_color = Color('beige')  # 设置颜色

    pygame.init()  # 初始化


    old_k_delay, old_k_interval = pygame.key.get_repeat ()
    pygame.key.set_repeat (500, 30)

    try:
        screen = pygame.display.set_mode(win_size)
        screen.fill(background_color)
        pygame.display.flip()

        image = pygame.image.load(image_file).convert()
        image_w, image_h = image.get_size()

        if image_w < view_size[0] or image_h < view_size[1]:
            print ("The source image is too small for this example.")
            print ("A %i by %i or larger image is required." % zoom_view_size)
            return

        regions = pygame.Surface(win_size, 0, 24)
        add_arrow_button(screen, regions, (40, win_size[1] // 2), 3)
        add_arrow_button(screen, regions, (win_size[0] - 40, win_size[1] // 2), 4)
        add_arrow_button(screen, regions, (win_size[0] // 2, 40), 1)
        add_arrow_button(screen, regions, (win_size[0] // 2, win_size[1] - 40), 2)
        pygame.display.flip()
        screen.set_clip((margin, margin, zoom_view_size[0], zoom_view_size[1]))
        view_rect = Rect(0, 0, view_size[0], view_size[1])
        scale(image.subsurface(view_rect), zoom_view_size, screen.subsurface(screen.get_clip()))
        pygame.display.flip()
        direction = None
        clock = pygame.time.Clock()
        clock.tick()

        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        going = False
                    elif e.key == K_DOWN:
                        scroll_view(screen, image, 2, view_rect)
                    elif e.key == K_UP:
                        scroll_view(screen, image, 1, view_rect)
                    elif e.key == K_LEFT:
                        scroll_view(screen, image, 3, view_rect)
                    elif e.key == K_RIGHT:
                        scroll_view(screen, image, 4, view_rect)
                elif e.type == QUIT:
                    going = False
                elif e.type == MOUSEBUTTONDOWN:
                    direction = regions.get_at(e.pos)[0]
                elif e.type == MOUSEBUTTONUP:
                    direction = None

            if direction:
                scroll_view(screen, image, direction, view_rect)
            clock.tick(30)

    finally:
        pygame.key.set_repeat (old_k_delay, old_k_interval)
        pygame.quit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        image_file = sys.argv[1]
    else:
        image_file = None
    main(image_file)
