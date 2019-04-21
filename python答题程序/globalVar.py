import os
import random
import sys
from xml.dom.minidom import parse
import pygame


class GlobalVar:
    def __init__(self):
        self.gameName = '大脑很囧'
        self.titleLabel = self.gameName + ' Version 1.3.1Dev'
        # 颜色字典
        self.color_dict = {'red': (255, 0, 0),  # 纯红
                           'blue': (255, 0, 0),  # 纯蓝
                           'green': (0, 125, 0),  # 纯绿
                           'lime': (0, 255, 0),  # 酸橙色
                           'gold': (255, 215, 0),  # 金色
                           'orange': (255, 165, 0),  # 橙色
                           'black': (0, 0, 0),  # 纯黑
                           'white': (255, 255, 255),  # 纯白
                           }

        # 初始化
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1024, 640))
        pygame.display.set_icon(pygame.image.load('img/delbrucks-brain.ico'))
        pygame.display.set_caption(self.titleLabel)

        self.titleFont = pygame.font.Font('font/YaHei.ttf', 150)
        self.aboutFont = pygame.font.Font('font/YaHei.ttf', 20)
        self.globalFont = pygame.font.Font('font/Hei.ttf', 36)
        self.questionFont = pygame.font.Font('font/HuaKanSong.ttf', 24)
        self.answerFont = pygame.font.Font('font/HuaKanSong.ttf', 22)
        self.helpFont = pygame.font.Font('font/HuaKanSong.ttf', 24)

        self.FPS = 30
        self.FPSCLOCK = pygame.time.Clock()

    def load_file(self, filename, totalNum):
        assert os.path.exists(filename), '题库文件: %s 不存在，游戏无法执行。' % (filename)
        # 读取xml文件中的题库
        question_data = parse(filename)
        # 得到根节点
        root = question_data.documentElement

        game_level = []
        questions = root.getElementsByTagName("question")

        for item in questions:
            q_list = {}
            answerList = []
            question = item.getAttribute("title")
            answer_items = item.getElementsByTagName("answer")  # 返回一个列表
            answerList.append(answer_items[0].getElementsByTagName("a")[0].childNodes[0].data)
            answerList.append(answer_items[0].getElementsByTagName("b")[0].childNodes[0].data)
            answerList.append(answer_items[0].getElementsByTagName("c")[0].childNodes[0].data)
            answerList.append(answer_items[0].getElementsByTagName("d")[0].childNodes[0].data)
            correct = item.getElementsByTagName("correct")[0].childNodes[0].data
            q_list['question'] = question
            q_list['answers'] = answerList
            q_list['correct'] = correct
            game_level.append(q_list)

        # 生产随机指定数量的题集，利用set的去重特性，这样当set的长度是10时，就是10个不重复的数字
        tmp_level = set()
        while len(tmp_level) < totalNum:
            randNum = random.randint(0, len(game_level) - 1)
            tmp_level.add(randNum)

        new_question = []
        for i in tmp_level:
            new_question.append(game_level[i])

        # 因为set的缘故，提取出来的题目是按顺序排列的，需要打乱一次,形成每次游戏时的题目顺序的独特随机性
        random.shuffle(new_question)

        return new_question

    def close_program(self):
        pygame.quit()
        sys.exit(0)

    def maketext(self, font, text, color):
        text_img = font.render(text, True, color)
        text_rect = text_img.get_rect()
        return text_img, text_rect
