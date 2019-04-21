import random

from SettingVar import SettingVar

setting = SettingVar()


def init_game():
    """初始化游戏的数组，于开始新游戏或者重置游戏时调用"""
    gameArray = [[0 for i in range(setting.WINDOW_BLOCK_NUM)] for j in
                 range(setting.WINDOW_BLOCK_NUM)]  # 初始化的游戏数组

    random_elem = 0
    while random_elem < 2: # 初始化两个开始元素在任意位置。
        add_elem(gameArray)  #添加一个元素2
        random_elem += 1

    return gameArray


def add_elem(gameArray):
    """添加元素功能"""
    while can_add_elem(gameArray):  #判断数组是否已经充满
        x = random.randint(0, setting.WINDOW_BLOCK_NUM - 1)# 生产随机位置元素，完成即跳出运行
        y = random.randint(0, setting.WINDOW_BLOCK_NUM - 1)
        if gameArray[x][y] == 0: # 判断该位置是否有0，无零的时候才添加
            gameArray[x][y] = 2  #添加
            break  # 添加完之后结束循环

def can_add_elem(gameArray):
    """初始化元素为零的元素数量为16个。每查找到一个非零的元素，计数减1. 如果没有是零的元素，不必添加新元素"""
    num_zero = 16
    # 添加一个判断，如果数组全部非0，不添加元素
    for i in range(setting.WINDOW_BLOCK_NUM):   # 双重循环遍历 每一个元素
        for j in range(setting.WINDOW_BLOCK_NUM):
            if gameArray[i][j] != 0:  # 统计还剩0的个数
                num_zero -= 1
    if num_zero == 0:  # 如果没有空位置了，则不进行添加
        return False
    return True


def can_move(gameArray):
    """检查是否可以移动，逻辑比较简单，就是逐个元素判断上下左右是否有相同的元素，如果可以存在，就是可以移动。否则就是不能移动"""
    for i in range(setting.WINDOW_BLOCK_NUM):  #双重for循环每一个元素
        for j in range(setting.WINDOW_BLOCK_NUM):
            if gameArray[i][j] != 0:
                return True
            elif gameArray[i][j] == gameArray[i][j + 1]:
                return True
            elif gameArray[i][j] == gameArray[i][j - 1]:
                return True
            elif gameArray[i][j] == gameArray[i + 1][j]:
                return True
            elif gameArray[i][j] == gameArray[i - 1][j]:
                return True
            else:
                return False


def is_win(gameArray):
    """遍历数组，如果里面有一个元素是2048，就表示胜利"""
    for i in range(setting.WINDOW_BLOCK_NUM):     # 双层for循环遍历里面的每一个元素
        for j in range(setting.WINDOW_BLOCK_NUM):
            if gameArray[i][j] == 2048:  # 若有一个等于2048 则胜利
                return True
            else:  # 否则，还未胜利
                return False
