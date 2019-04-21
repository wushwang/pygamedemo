import pygame

from AboutThis import about_this
from GameEnd import end_game
from GameLoad import load_game
from globalVar import GlobalVar
from GameTitle import game_title


def main():
    globalVar = GlobalVar()
    SURFACE = globalVar.SCREEN
    result = game_title(SURFACE, globalVar, )  # 游戏从初始的标题开始。所以这个直接载入，不需要添加到循环中去。

    totalNum = 10
    corrent = 0
    score = 0
    right_score = 0
    wrong_score = 0
    gameLevels = None
    while True:

        if 'reset' in result:
            # 返回到游戏标题界面
            result = game_title(SURFACE, globalVar)
        elif 'start' in result:
            gameLevels = globalVar.load_file("data.xml", totalNum)  # 在点开始游戏的时候载入10道题
            pygame.time.wait(1000)  # 和答题同理
            corrent = 0  # 开始游戏的时候，将当前的题目设置为第1条，如果不这样做初始化，得到的都是最后的一道题
            result = load_game(SURFACE, globalVar, gameLevels, corrent, score, right_score, wrong_score)
        elif 'about' in result:
            result = about_this(SURFACE, globalVar)
        elif result in ('next', 'yes', 'no'):
            pygame.time.wait(1000)  # 答题完成后，给定一个等待时间，有效防止题目下一题刷出来还没有看就点中了答案
            # 先计分，否则最后的统计会因为少统计了一条而出错
            if result in 'yes':
                score += 100
                right_score += 1
            elif result in 'no':
                wrong_score += 1

            if corrent == len(gameLevels) - 1:
                result = end_game(SURFACE, globalVar, score, right_score, totalNum)
            else:
                corrent += 1
                result = load_game(SURFACE, globalVar, gameLevels, corrent, score, right_score, wrong_score)
        else:
            # 为添加新功能预留
            pass

        pygame.display.update()
        pygame.time.Clock().tick(30)

'''运行此程序，开始游戏'''
if __name__ == '__main__':
    main()
