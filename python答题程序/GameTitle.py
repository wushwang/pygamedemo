import pygame
from pygame.locals import *


def game_title(SURFACE,globalVar):
    title_text = '我学Python'
    bt_start_text = '开 始 游 戏'
    bt_about_text = '关 于 游 戏'
    title_bg = pygame.image.load('img/main.jpg')
    title_image = globalVar.titleFont.render(title_text, True, globalVar.color_dict['green'])
    title_time = 0
    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()  # 加载鼠标图片

    while True:
        SURFACE.blit(title_bg, (0, 0))
        if title_time == 0:
            title_image = globalVar.titleFont.render(title_text, True, globalVar.color_dict['white'])
            title_time = 1
        elif title_time == 1:
            title_image = globalVar.titleFont.render(title_text, True, globalVar.color_dict['green'])
            title_time = 2
        elif title_time == 2:
            title_image = globalVar.titleFont.render(title_text, True, globalVar.color_dict['lime'])
            title_time = 0
        title_rect = title_image.get_rect()
        title_rect.centerx = SURFACE.get_rect().centerx
        title_rect.top = 130

        tips_image = globalVar.globalFont.render(bt_start_text, True, globalVar.color_dict['orange'])
        tips_rect = tips_image.get_rect()
        tips_rect.centerx = SURFACE.get_rect().centerx - 150
        tips_rect.top = 400

        help_image = globalVar.globalFont.render(bt_about_text, True, globalVar.color_dict['orange'])
        help_rect = help_image.get_rect()
        help_rect.centerx = SURFACE.get_rect().centerx + 150
        help_rect.top = 400

        SURFACE.blit(title_image, title_rect)
        SURFACE.blit(tips_image, tips_rect)
        SURFACE.blit(help_image, help_rect)

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                globalVar.close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    globalVar.close_program()

        x, y = pygame.mouse.get_pos()
        pressed_array = pygame.mouse.get_pressed()  # 获取鼠标事件的列表

        # 开始按键的鼠标事件，包括了鼠标经过事件和点击事件
        if tips_rect.left < x < tips_rect.right and tips_rect.top < y < tips_rect.bottom:
            tips_image = globalVar.globalFont.render(bt_start_text, True, globalVar.color_dict['red'])
            SURFACE.blit(tips_image, tips_rect)
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'start'

        # 关于按键的鼠标事件
        if help_rect.left < x < help_rect.right and help_rect.top < y < help_rect.bottom:
            help_image = globalVar.globalFont.render(bt_about_text, True, globalVar.color_dict['red'])
            SURFACE.blit(help_image, help_rect)
            for event in pressed_array:
                if event == 1:  # 1为鼠标左键点击事件
                    return 'about'

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)

        x -= 0
        y -= 0

        SURFACE.blit(mouseCursor, (x, y))
        pygame.display.update()
        pygame.time.Clock().tick(20)
