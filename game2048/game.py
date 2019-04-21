import sys

import pygame

from GameFunction import init_game, add_elem, can_move, is_win
from SettingVar import SettingVar
from game_draw import draw_background, draw_game

setting = SettingVar()  # 获取颜色、数字的配置信息


def main():
    global screen, tileFont, titleFont, normalFont  # 定义全局变量

    pygame.init()  # 初始化工具箱
    screen = pygame.display.set_mode((800, 600))  # 生成一个800*600的窗口
    pygame.display.set_caption('游戏2048')  # 设置游戏的标题

    font_path = 'c:\\windows\\Fonts\\SimHei.ttf'  # 字体文件路径
    tileFont = pygame.font.Font(font_path, 36)  # 生成不同大小的字体
    titleFont = pygame.font.Font(font_path, 48)
    normalFont = pygame.font.Font(font_path, 24)

    titleText = titleFont.render('游戏2048', True, setting.COLOR_DICT['gray'])  # 渲染文本“游戏2048”
    titleRect = titleText.get_rect()  # 得到文字的文本框
    titleRect.topleft = 570, 60  # 设置文本的左上角顶点坐标（570，60）

    btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['tomato'])  # 同上
    btStartRect = btStartText.get_rect()
    btStartRect.topleft = 620, 400

    btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['tomato'])
    btResetRect = btResetText.get_rect()
    btResetRect.topleft = 620, 440

    btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['tomato'])
    btExitRect = btExitText.get_rect()
    btExitRect.topleft = 620, 480

    gameArray = init_game()  # 定义存储数字的二维列表

    gamestatus = None  # 设置游戏状态，开始为None,分为“start”，“win”，“lost”

    while True:

        draw_background(screen, titleText, titleRect, btStartText, btStartRect, btResetText, btResetRect, btExitText,
                        btExitRect)  # 调用画背景的方法

        if gamestatus == 'start':  # 判断是否开始游戏
            draw_game(screen, tileFont, gameArray)  # 调用游戏开始的方法
        elif gamestatus == 'win':  # 判断游戏是否赢
            pass
        elif gamestatus == 'lost':  # 判断游戏是否输
            pass
        else:
            pass

        for event in pygame.event.get():  # 处理事件
            if event.type == pygame.QUIT:  # 退出事件
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP:  # 空格键退出
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                elif event.key in (pygame.K_a, pygame.K_LEFT):  # 判断是否按下左键或a
                    for i in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从右边开始往左边移动，不然只移动一格
                        if i > 0:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                while gameArray[i][j] != 0 and gameArray[i - 1][j] == 0:
                                    gameArray[i - 1][j] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                if gameArray[i][j] == gameArray[i - 1][j]:
                                    gameArray[i - 1][j] += gameArray[i][j]
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_d, pygame.K_RIGHT):  # 判断是否按下d或右键
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        if i < setting.WINDOW_BLOCK_NUM - 1:
                            for j in range(setting.WINDOW_BLOCK_NUM):
                                while gameArray[i][j] != 0 and gameArray[i + 1][j] == 0:
                                    gameArray[i + 1][j] = gameArray[i][j]
                                    gameArray[i][j] = 0

                                if gameArray[i][j] == gameArray[i + 1][j]:
                                    gameArray[i + 1][j] += gameArray[i][j]
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_w, pygame.K_UP):  # 判断是否按下w 或 上
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in reversed(range(setting.WINDOW_BLOCK_NUM)):  # 要反序从上面往下面移动，不然只移动一格
                            if j > 0:
                                if gameArray[i][j] != 0 and gameArray[i][j - 1] == 0:
                                    gameArray[i][j - 1] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                if gameArray[i][j] == gameArray[i][j - 1]:
                                    gameArray[i][j - 1] += gameArray[i][j]
                                    gameArray[i][j] = 0
                    add_elem(gameArray)

                elif event.key in (pygame.K_s, pygame.K_DOWN):  # 判断是否按下下或s键
                    for i in range(setting.WINDOW_BLOCK_NUM):
                        for j in range(setting.WINDOW_BLOCK_NUM):
                            if j < setting.WINDOW_BLOCK_NUM - 1:
                                # 移动元素
                                if gameArray[i][j] != 0 and gameArray[i][j + 1] == 0:
                                    gameArray[i][j + 1] = gameArray[i][j]
                                    gameArray[i][j] = 0
                                # 合并元素
                                if gameArray[i][j] == gameArray[i][j + 1]:
                                    gameArray[i][j + 1] += gameArray[i][j]
                                    gameArray[i][j] = 0
                    add_elem(gameArray)
            if not can_move(gameArray):  # 判断二维列表是否可以移动，不能移动就输了
                print('lost')
            if is_win(gameArray):  # 判断列表是否赢了
                print('win')

            # 右侧的按键的鼠标事件
            x, y = pygame.mouse.get_pos()  # 获取鼠标的位置
            pressed = pygame.mouse.get_pressed()  # 获取按下的鼠标键

            if btStartRect.collidepoint(x, y):  # 判断鼠标是否在“开始游戏”上碰撞
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['yellow'])  # 改变字体的颜色
                for event in pressed:  # 遍历事件
                    if event == 1:  # 若点击了左键
                        gameArray = init_game()  # 初始化的游戏数组
                        gamestatus = 'start'  # 设置游戏状态，开始游戏
            else:
                btStartText = normalFont.render('开始游戏', True, setting.COLOR_DICT['tomato'])

            if btResetRect.collidepoint(x, y):  # 同上
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        gameArray = init_game()  # 初始化的游戏数组
            else:
                btResetText = normalFont.render('重置游戏', True, setting.COLOR_DICT['tomato'])

            if btExitRect.collidepoint(x, y):  # 同上
                btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['yellow'])
                for event in pressed:
                    if event == 1:
                        pygame.quit()
                        sys.exit(0)
            else:
                btExitText = normalFont.render('退出游戏', True, setting.COLOR_DICT['tomato'])

        pygame.display.update()  # 刷新屏幕
        pygame.time.Clock().tick(30)  # 设置每秒执行30次循环


'''运行此程序开始游戏'''
if __name__ == '__main__':
    main()
