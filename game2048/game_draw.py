import pygame
from SettingVar import SettingVar
setting = SettingVar()


def draw_game(screen, tileFont, gameArray):
    """完成游戏元素的绘制"""
    for i in range(len(gameArray)):  # 双重循环遍历二维列表里面的每一个元素
        for j in range(len(gameArray[0])):
            if gameArray[i][j] != 0:  # 判断元素是否为0
                tile = pygame.draw.rect(screen, setting.COLOR_DICT['silver'],
                                        ((setting.TILE_SIZE + 20) * i + 110, (setting.TILE_SIZE + 20) * j + 110,
                                         setting.TILE_SIZE, setting.TILE_SIZE))  # 画矩形框
                tile_text = str(gameArray[i][j])  # 将元素数字转换成字符串
                text = tileFont.render(tile_text, True, setting.NUM_COLOR_DICT[tile_text])  # 渲染
                text_rect = text.get_rect()  # 获取元素文字框
                text_rect.center = tile.center  # 获取元素文字矩形框
                screen.blit(text, text_rect)  # 输出元素


def draw_background(screen, titleText, titleRect, btStartText, btStartRect, btResetText, btResetRect, btExitText,
                    btExitRect):
    """绘制网格和按键，标题等"""
    screen.fill(setting.COLOR_DICT['bisque'])  # 填充背景色

    screen.blit(titleText, titleRect)  # 输出‘游戏2048’
    screen.blit(btStartText, btStartRect)  # 输出“开始游戏”
    screen.blit(btResetText, btResetRect)  # 输出“重置游戏”
    screen.blit(btExitText, btExitRect)  # 输出结束游戏

    # 五条横线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (500, 100), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 200), (500, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 300), (500, 300), 2)

    pygame.draw.line(screen, (0, 0, 0), (100, 400), (500, 400), 2)
    pygame.draw.line(screen, (0, 0, 0), (100, 500), (500, 500), 2)

    # 五条竖线
    pygame.draw.line(screen, (0, 0, 0), (100, 100), (100, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (200, 100), (200, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (300, 100), (300, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (400, 100), (400, 500), 2)
    pygame.draw.line(screen, (0, 0, 0), (500, 100), (500, 500), 2)
