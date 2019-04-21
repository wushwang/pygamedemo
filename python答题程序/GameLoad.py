import pygame
from pygame.locals import *


def load_game(SURFACE, globalVar, gameLevels, current, total_score, total_right_score, total_wrong_score):
    SURFACE.fill(globalVar.color_dict['black'])
    title_bg = pygame.image.load('img/title.jpg')

    level = gameLevels[current]
    level_question = level['question']
    level_answer = level['answers']
    level_correct = int(level['correct'])

    bt_replay = pygame.Rect((0, 0), (220, 50))
    bt_replay.left = 730
    bt_replay.top = 400
    # replay_img = globalVar.globalFont.render('重新开始', True, globalVar.color_dict['white'])
    # replay_rect = replay_img.get_rect()
    replay_img, replay_rect = globalVar.maketext(globalVar.globalFont, '重新开始', globalVar.color_dict['white'])
    replay_rect.center = bt_replay.center

    bt_exit = pygame.Rect((0, 0), (220, 50))
    bt_exit.left = 730
    bt_exit.top = 480
    # exit_img = globalVar.globalFont.render('结束游戏', True, globalVar.color_dict['white'])
    # exit_rect = exit_img.get_rect()
    exit_img, exit_rect = globalVar.maketext(globalVar.globalFont, '结束游戏', globalVar.color_dict['white'])
    exit_rect.center = bt_exit.center

    mouseCursor = pygame.image.load('img/cursor.png').convert_alpha()  # 载入鼠标的图片

    while True:

        SURFACE.blit(title_bg, (0, 0))

        # 显示出问题,按照宽度是25个字符串的规格显示出来。
        for i in range(int(len(level_question) / 25 + 1)):
            start = i * 25
            end = (i + 1) * 25
            question_image = globalVar.questionFont.render(level_question[start:end], True,
                                                           globalVar.color_dict['black'])
            SURFACE.blit(question_image, (50, 80 + (i * 30)))

        # 右侧的内容
        level_image = globalVar.helpFont.render('当前题目：第 ' + str(current + 1) + ' 题', True,
                                                globalVar.color_dict['orange'])
        SURFACE.blit(level_image, (725, 80))
        score_image = globalVar.helpFont.render('当前分数：' + str(total_score), True, globalVar.color_dict['orange'])
        SURFACE.blit(score_image, (725, 120))
        score_image = globalVar.helpFont.render('正确题数：' + str(total_right_score), True, globalVar.color_dict['orange'])
        SURFACE.blit(score_image, (725, 160))
        score_image = globalVar.helpFont.render('错误题数：' + str(total_wrong_score), True, globalVar.color_dict['orange'])
        SURFACE.blit(score_image, (725, 200))

        # 显示出答案选项
        item1_image = globalVar.answerFont.render('1、 ' + level_answer[0], True, globalVar.color_dict['red'])
        item1_rect = item1_image.get_rect()

        item1_rect.left = 50
        item1_rect.top = 310
        item2_image = globalVar.answerFont.render('2、 ' + level_answer[1], True, globalVar.color_dict['red'])
        item2_rect = item2_image.get_rect()

        item2_rect.left = 50
        item2_rect.top = 380
        item3_image = globalVar.answerFont.render('3、 ' + level_answer[2], True, globalVar.color_dict['red'])
        item3_rect = item3_image.get_rect()

        item3_rect.left = 50
        item3_rect.top = 450
        item4_image = globalVar.answerFont.render('4、 ' + level_answer[3], True, globalVar.color_dict['red'])
        item4_rect = item4_image.get_rect()

        item4_rect.left = 50
        item4_rect.top = 520

        SURFACE.blit(item1_image, item1_rect)
        SURFACE.blit(item2_image, item2_rect)
        SURFACE.blit(item3_image, item3_rect)
        SURFACE.blit(item4_image, item4_rect)

        pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_replay)
        pygame.draw.rect(SURFACE, globalVar.color_dict['lime'], bt_exit)

        SURFACE.blit(replay_img, replay_rect)
        SURFACE.blit(exit_img, exit_rect)

        for event in pygame.event.get():
            # 关闭按钮的事件
            if event.type == QUIT:
                globalVar.close_program()
            elif event.type == KEYDOWN:
                # 按键按下后抬起的事件判断
                if event.key == K_ESCAPE:
                    globalVar.close_program()
                # elif event.key == K_BACKSPACE:
                #     # 按回退键，返回到标题界面。
                #     return 'reset'
                # elif event.key == K_RETURN:
                #     # 按回车键，跳到下一题。
                #     return 'next'

        # 鼠标控制事件
        x, y = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        # 四个答案区域的内容的鼠标事件控制
        # 最开始的使用是判断鼠标的坐标是否在图形的上下左右的范围内
        # 之后修改为直接调用碰撞检测，减少了写 left < x < right and top < y < bottom 这样的判断，直接使用了collidepoint()
        if item1_rect.collidepoint(x, y):
            item1_image = globalVar.answerFont.render('1 - ' + level_answer[0], True, globalVar.color_dict['gold'])
            SURFACE.blit(item1_image, item1_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 1:
                        return 'yes'
                    else:
                        return 'no'
        if item2_rect.collidepoint(x, y):
            item2_image = globalVar.answerFont.render('2 - ' + level_answer[1], True, globalVar.color_dict['gold'])
            SURFACE.blit(item2_image, item2_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 2:
                        return 'yes'
                    else:
                        return 'no'
        if item3_rect.collidepoint(x, y):
            item3_image = globalVar.answerFont.render('3 - ' + level_answer[2], True, globalVar.color_dict['gold'])
            SURFACE.blit(item3_image, item3_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 3:
                        return 'yes'
                    else:
                        return 'no'
        if item4_rect.collidepoint(x, y):
            item4_image = globalVar.answerFont.render('4 - ' + level_answer[3], True, globalVar.color_dict['gold'])
            SURFACE.blit(item4_image, item4_rect)
            for event in pressed:
                if event == 1:
                    if level_correct == 4:
                        return 'yes'
                    else:
                        return 'no'
        # 右侧按键的鼠标事件
        if bt_replay.collidepoint(x, y):
            pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_replay)
            for event in pressed:
                if event == 1:
                    return 'reset'
        if bt_exit.collidepoint(x, y):
            pygame.draw.rect(SURFACE, globalVar.color_dict['orange'], bt_exit)
            for event in pressed:
                if event == 1:
                    globalVar.close_program()

        # 自定义鼠标样式
        pygame.mouse.set_visible(False)
        x -= 0
        y -= 0
        SURFACE.blit(mouseCursor, (x, y))

        pygame.display.update()
        pygame.time.Clock().tick(30)
