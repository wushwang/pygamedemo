from ball_ball_class import *
from ball_player import *

pygame.init()  # 初始化pygame窗口
pygame.mixer.init()  # 初始化声音

win_x = 800  # 初始化窗口尺寸
win_y = 500
win = pygame.display.set_mode((win_x, win_y))  # 创建pygame窗口
pygame.display.set_caption("会玩球的小丑")  # pygame窗口名称

# 游戏说明

# 游戏文字
text = ["Game Over!",
        "New Hi-Score!",
        "P1:",
        "Hi-Score:",
        "P2:",
        "P1 wins!",
        "P2 wins!",
        "P1 wins with hi-score!",
        "P2 wins with hi-score!",
        "Oops!  Tie game!",
        "Tie game, but with hi-score!"]

clock = pygame.time.Clock()  # 初始化时间变量
score = 0  # 得分变量球员1
score2 = 0  # 得分变量玩家2
gameOv = 0  # 结束游戏变量
play = 0  # 游戏的计数器
global hiScoreOld  # 记录最高得分的变量
with open("hiScoreLog.txt") as h:  # 读取最高得分的文件
    for line in h:
        hiScoreOld = line
hiScore = int(hiScoreOld)
c = 0
d = 0

# 字体
font = pygame.font.SysFont('arial', 30, True, True)
font2 = pygame.font.SysFont('arial', 100, False, True)
font3 = pygame.font.SysFont('arial', 20, False, True)

# 渲染游戏文字
onScreen = [font2.render(text[0], 1, (128, 0, 0)),
            font2.render(text[1], 1, (128, 0, 0)),
            font3.render(text[2], 1, (0, 128, 0)),
            font3.render(text[3], 1, (0, 0, 0)),
            font3.render(text[4], 1, (0, 0, 128)),
            font.render(text[5], 1, (0, 128, 0)),
            font.render(text[6], 1, (0, 0, 128)),
            font.render(text[7], 1, (0, 128, 0)),
            font.render(text[8], 1, (0, 0, 128)),
            font.render(text[9], 1, (0, 0, 0)),
            font.render(text[10], 1, (0, 0, 0))]

# 初始化所有声音
intro = pygame.mixer.Sound('sounds/sms-alert-2-daniel_simon.wav')
whoosh = pygame.mixer.Sound('sounds/Woosh-Mark_DiAngelo-4778593.wav')
catch = pygame.mixer.Sound('sounds/Ball_Bounce-Popup_Pixels-172648817.wav')
drop = pygame.mixer.Sound('sounds/Light Bulb Breaking-SoundBible.com-53066515.wav')
hi = pygame.mixer.Sound('sounds/Ta Da-SoundBible.com-1884170640.wav')


def redraw_game_window():  # 在游戏窗口中重绘所有内容的功能
    global hiScoreOld
    pygame.Surface.fill(win, (255, 255, 255))  # 保持背景白色
    # 分数文字
    scores = [font3.render(str(score), 1, (0, 0, 0)),
              font3.render(str(hiScore), 1, (0, 0, 0)),
              font3.render(str(score2), 1, (0, 0, 0))]
    if play == 0:
        j = font3.render(u'1选择角色1，2选择角色2，ESC退出，空格开始，左右伸手臂', 1, (0, 0, 0))
        win.blit(j, (win_x // 2 - (j.get_width() / 2), 23 + 10))
    elif play == 1:  # 单人游戏说明
        for z in balls:
            z.visibility = False  # 让球再次隐形
    elif play == 3:
        for z in balls:
            z.visibility = False
    elif play == 5:
        for z in balls:
            z.visibility = False
    elif play == 7:
        for z in balls:
            z.visibility = False  # 游戏停在这里

    win.blit(onScreen[2], (10, 10))  # 在屏幕上呈现文本
    win.blit(scores[0], (onScreen[2].get_width() + 10, 10))
    win.blit(onScreen[3], (win_x // 2 - (onScreen[3].get_width() / 2), 10))
    win.blit(scores[1], (win_x // 2 + (onScreen[3].get_width() / 2) + 2, 10))
    win.blit(onScreen[4], (win_x - 50, 10))
    win.blit(scores[2], (win_x - 28, 10))
    l_arm.draw(win)  # 画臂
    r_arm.draw(win)
    hands[0].draw(win)  # 画手
    hands[1].draw(win)
    for ball in balls:  # 画球
        ball.draw(win)
    man.draw(win)  # 画我们的玩家
    if gameOv == 1:  # 如果gameOver变量为1，则打印“Game Over”
        win.blit(onScreen[0], (win_x // 2 - (onScreen[0].get_width() / 2), win_y - 400))  # 显示消息
        if int(hiScoreOld) < hiScore:
            win.blit(onScreen[1], (win_x // 2 - (onScreen[1].get_width() / 2), win_y - 300))
        else:
            pass
    elif gameOv == 2:  # 如果玩家点击ESC，则显示此消息
        win.blit(onScreen[0], (win_x // 2 - (onScreen[0].get_width() / 2), win_y - 400))
    elif gameOv == 3:  # 如果玩家1赢得2人游戏，则显示此消息
        win.blit(onScreen[5], (win_x // 2 - (onScreen[5].get_width() / 2), win_y - 300))
    elif gameOv == 4:  # 如果玩家2赢得2人游戏，则显示此消息
        win.blit(onScreen[6], (win_x // 2 - (onScreen[6].get_width() / 2), win_y - 300))
    elif gameOv == 5:  # 如果玩家1赢得高分的2人游戏，则显示此消息
        win.blit(onScreen[7], (win_x // 2 - (onScreen[7].get_width() / 2), win_y - 300))
    elif gameOv == 6:  # 如果玩家2赢得高分的双人游戏，则显示此消息
        win.blit(onScreen[8], (win_x // 2 - (onScreen[8].get_width() / 2), win_y - 300))
    elif gameOv == 7:  # 如果得分最终结合，则显示此消息
        win.blit(onScreen[9], (win_x // 2 - (onScreen[9].get_width() / 2), win_y - 300))
    elif gameOv == 8:  # 如果得分相关，则显示此消息，但有新的高分
        win.blit(onScreen[10], (win_x // 2 - (onScreen[10].get_width() / 2), win_y - 300))
    pygame.display.update()  # 不断更新显示


man = player(win_x // 2 - 32, win_y - 100, 64, 64)  # 创建玩家
ball1 = ball(man.x + 26, man.y + 36, 12, 12, 102, 0)  # 初始化球和球列表
ball2 = ball(man.x + 26, man.y + 36, 12, 12, 201.5, 1)
ball3 = ball(man.x + 26, man.y + 36, 12, 12, 301, 2)
balls = [ball1, ball2, ball3]

# 初始化所有arm变量
l_arms = [arm([(man.x + 32, man.y + 42), (man.x + 32 - z * 50, man.y + 64),
               (man.x + 32 - z * 50, man.y + 64), (man.x + 32 - z * 100, man.y + 42)])  # 创建左胳膊
          for z in range(1, 4)]
r_arms = [arm([(man.x + 32, man.y + 42), (man.x + 32 + z * 50, man.y + 64),
               (man.x + 32 + z * 50, man.y + 64), (man.x + 32 + z * 100, man.y + 42)])
          for z in range(1, 4)]
l_arm = l_arms[c]
r_arm = r_arms[d]
hands = [hand(l_arm.getCoords()[3][0] - 16, l_arm.getCoords()[3][1] - 32, 32, 32, False),
         hand(r_arm.getCoords()[3][0] - 16, r_arm.getCoords()[3][1] - 32, 32, 32, True)]  # 初始化手
intro.play()  # 播放音乐
run = True  # 设置游戏状态
while run:
    clock.tick(10)  # 设置游戏每秒循环10次
    for ball in balls:  # 检查球是否已经掉落
        if ball.visibility == True:
            if ball.getCoords()[1] + 12 >= hands[0].y:
                if ball.getCoords()[0] + 12 >= hands[0].x and ball.getCoords()[0] + 12 <= hands[0].x + 32:
                    if play == 2 or play == 4:
                        score += 10  # 如果球被抓住则增加分数
                    elif play == 6:
                        score2 += 10
                    catch.play()  # 播放声音
                    ball.caughtBall(True)  # 改变球被抓住的一面
                    whoosh.play()  # 发出嗖嗖声
                elif ball.getCoords()[0] + 12 >= hands[1].x and ball.getCoords()[0] + 12 <= hands[1].x + 32:
                    if play == 2 or play == 4:
                        score += 10
                    elif play == 6:
                        score2 += 10
                    catch.play()
                    ball.caughtBall(False)
                    whoosh.play()
                else:
                    # 如果其中一个球落下，游戏就结束了
                    if play == 2:
                        # 单人游戏结束
                        gameOv = 1
                        play = 7  # 明确停止游戏
                        if hiScore < score:
                            hi.play()  # 播放破纪录声音
                            hiScore = score  # 更新最高分
                            with open("hiScoreLog.txt", mode='a') as h:
                                h.write(str(hiScore) + '\n')
                        else:
                            drop.play()  # 播放失败的声音
                    elif play == 4:
                        play = 5
                        drop.play()
                    else:
                        # 玩家2的游戏结束。输出适当的消息
                        # 取决于哪个玩家获胜
                        play = 7
                        if score > score2:
                            if score > hiScore:
                                gameOv = 5  # 球员1获得高分
                                # 在日志中记录新的高分
                                hi.play()
                                hiScore = score
                                with open("hiScoreLog.txt", mode='a') as h:
                                    h.write(str(hiScore) + '\n')
                            else:
                                gameOv = 3  # 球员1胜，没有高分
                                drop.play()
                        elif score < score2:
                            if hiScore < score2:
                                gameOv = 6  # 球员2获得高分
                                hi.play()
                                hiScore = score2
                                with open("hiScoreLog.txt", mode='a') as h:
                                    h.write(str(hiScore) + '\n')
                            else:
                                drop.play()  # 播放声音
                                gameOv = 4  # 球员2胜，没有高分
                        else:
                            if hiScore < score:
                                gameOv = 8  # 分数相等，但新的高分
                                hi.play()
                                hiScore = score
                                with open("hiScoreLog.txt", mode='a') as h:
                                    h.write(str(hiScore) + '\n')
                            else:
                                # 没有高分
                                drop.play()
                                gameOv = 7
    if score == 100 or score2 == 100:# 检查分数以添加其他球
        ball3.visibility = True
    for event in pygame.event.get():# 检查玩家是否退出游戏
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()  # 为按键创建变量句柄
    if keys[pygame.K_1]:
        if play == 0 or play == 7:
            # 用户启动2人游戏
            gameOv = 0  # 重置游戏结束条件
            play = 1  # 重置播放条件
            score = 0
            score2 = 0

    elif keys[pygame.K_2]:
        if play == 0 or play == 7:
            # User starts 2-player game
            gameOv = 0  # 重置游戏结束条件
            play = 3  # 重置播放条件
            score = 0
            score2 = 0

    if keys[pygame.K_SPACE]:
        if play == 1:
            play = 2

            with open("hiScoreLog.txt") as h:
                for line in h:
                    hiScoreOld = line

            c = 0
            d = 0
            l_arm = l_arms[c]
            r_arm = r_arms[d]
            hands[0].x = l_arm.getCoords()[3][0] - 16
            hands[0].y = l_arm.getCoords()[3][1] - 32
            hands[1].x = r_arm.getCoords()[3][0] - 16
            hands[1].y = r_arm.getCoords()[3][1] - 32

            for b in balls:
                b.setCoord(man.x + 26, man.y + 36, pi / 2)
                b.caughtBall(False)
            ball1.visibility = True
            ball2.visibility = True
            ball3.visibility = False

            whoosh.play()
        elif play == 3:
            play = 4  # Player 1 starts in 2-player game when user hits space
            c = 0
            d = 0
            l_arm = l_arms[c]
            r_arm = r_arms[d]
            hands[0].x = l_arm.getCoords()[3][0] - 16
            hands[0].y = l_arm.getCoords()[3][1] - 32
            hands[1].x = r_arm.getCoords()[3][0] - 16
            hands[1].y = r_arm.getCoords()[3][1] - 32

            for b in balls:
                b.setCoord(man.x + 26, man.y + 36, pi / 2)
                b.caughtBall(False)
            ball1.visibility = True
            ball2.visibility = True
            ball3.visibility = False

            whoosh.play()

        elif play == 5:
            play = 6  # Player 2 starts
            c = 0
            d = 0
            l_arm = l_arms[c]
            r_arm = r_arms[d]
            hands[0].x = l_arm.getCoords()[3][0] - 16
            hands[0].y = l_arm.getCoords()[3][1] - 32
            hands[1].x = r_arm.getCoords()[3][0] - 16
            hands[1].y = r_arm.getCoords()[3][1] - 32

            for b in balls:
                b.setCoord(man.x + 26, man.y + 36, pi / 2)
                b.caughtBall(False)
            ball1.visibility = True
            ball2.visibility = True
            ball3.visibility = False

            whoosh.play()

    if keys[pygame.K_LEFT]:
        if play == 2 or play == 4 or play == 6:
            if c < 2 and d > 0:
                if d == 1:
                    d -= 1
                    r_arm = r_arms[d]
                    hands[1].x = r_arm.getCoords()[3][0] - 16
                    hands[1].y = r_arm.getCoords()[3][1] - 32
                else:
                    c += 1
                    d -= 1
                    l_arm = l_arms[c]
                    r_arm = r_arms[d]
                    hands[0].x = l_arm.getCoords()[3][0] - 16
                    hands[0].y = l_arm.getCoords()[3][1] - 32
                    hands[1].x = r_arm.getCoords()[3][0] - 16
                    hands[1].y = r_arm.getCoords()[3][1] - 32
            elif c < 2 and d == 0:
                c += 1
                l_arm = l_arms[c]
                r_arm = r_arms[d]
                hands[0].x = l_arm.getCoords()[3][0] - 16
                hands[0].y = l_arm.getCoords()[3][1] - 32
                hands[1].x = r_arm.getCoords()[3][0] - 16
                hands[1].y = r_arm.getCoords()[3][1] - 32

    elif keys[pygame.K_RIGHT]:
        # Right key gets pressed
        # Extend right arm and contract left
        if play == 2 or play == 4 or play == 6:
            if d < 2 and c > 0:
                if c == 1:
                    # Fix left arm if arm outstrecthed
                    c -= 1
                    l_arm = l_arms[c]
                    hands[0].x = l_arm.getCoords()[3][0] - 16
                    hands[0].y = l_arm.getCoords()[3][1] - 32
                else:
                    d += 1
                    c -= 1
                    l_arm = l_arms[c]
                    r_arm = r_arms[d]
                    hands[0].x = l_arm.getCoords()[3][0] - 16
                    hands[0].y = l_arm.getCoords()[3][1] - 32
                    hands[1].x = r_arm.getCoords()[3][0] - 16
                    hands[1].y = r_arm.getCoords()[3][1] - 32
            elif d < 2 and c == 0:
                d += 1
                l_arm = l_arms[c]
                r_arm = r_arms[d]
                hands[0].x = l_arm.getCoords()[3][0] - 16
                hands[0].y = l_arm.getCoords()[3][1] - 32
                hands[1].x = r_arm.getCoords()[3][0] - 16
                hands[1].y = r_arm.getCoords()[3][1] - 32

    elif keys[pygame.K_ESCAPE]:
        # Escape key quits game.  Flash game over screen if ESC is pressed
        gameOv = 2
        play = 7  # Also stop game explicitly
        run = False
    else:
        pass

    redraw_game_window()  # Recall the redraw function if game playing

pygame.mixer.quit()  # stop mixer
pygame.quit()  # end pygame session
