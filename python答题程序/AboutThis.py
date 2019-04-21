import pygame
from pygame.locals import *


def about_this(SURFACE, globalVar):
    productName = '游戏名称：Python测试练习'
    programBy = '程序设计：Zhao li yin'
    guiDesing = 'UI设计：Zhao li yin'
    copyRight = 'CopyRight © Zhao li yin'

    aboutText = [productName, programBy, guiDesing, copyRight, '',
                 '本游戏使用python+pygame制作。', 'data.xml是试题文件及答案，可以按照文件内容，自行添加试题','']

    bg = pygame.image.load('img/about.png')  # 加载背景图片

    bt_back = pygame.Rect((0, 0), (180, 60))  # 绘制矩形框
    bt_back.left = 400  # 设置矩形框左边的距离
    bt_back.bottom = 580  # 设置矩形框底部的距离

    back_img, back_rect = globalVar.maketext(globalVar.globalFont, '返  回', globalVar.color_dict['red'])
    back_rect.center = bt_back.center

    while True:
        SURFACE.fill(globalVar.color_dict['black'])
        SURFACE.blit(bg, (0, 0))

        for item in aboutText:
            font_img, font_rect = globalVar.maketext(globalVar.aboutFont, item, globalVar.color_dict['red'])
            font_rect.top = 80 + aboutText.index(item) * 30
            font_rect.left = 300

            SURFACE.blit(font_img, font_rect)

        pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_back)

        for event in pygame.event.get():
            if event.type == QUIT:
                globalVar.close_program()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    globalVar.close_program()

        pygame.mouse.set_visible(True)

        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()

        if bt_back.collidepoint(x, y):
            pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_back)
            for event in pressed:
                if event == 1:
                    return 'reset'

        SURFACE.blit(back_img, back_rect)

        pygame.display.update()
        pygame.time.Clock().tick(30)
