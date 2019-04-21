class SettingVar:
    def __init__(self):
        # 颜色词典
        self.COLOR_DICT = {'white': (255, 255, 255),  # 白色
                           'ivory': (255, 255, 240),  # 象牙色
                           'yellow': (255, 255, 0),  # 黄色
                           'seashell': (255, 245, 238),  # 海贝色
                           'bisque': (255, 228, 196),  # 橘黄色
                           'gold': (255, 215, 0),  # 金色
                           'pink': (255, 192, 203),  # 粉红色
                           'lightpink': (255, 182, 193),  # 亮粉红色
                           'orange': (255, 165, 0),  # 橙色
                           'coral': (255, 127, 80),  # 珊瑚色
                           'tomato': (255, 99, 71),  # 番茄色
                           'magenta': (255, 0, 255),  # 洋红色
                           'wheat': (245, 222, 179),  # 小麦色
                           'violet': (238, 130, 238),  # 紫罗兰色
                           'silver': (192, 192, 192),  # 银白色
                           'brown': (165, 42, 42),  # 棕色
                           'gray': (128, 128, 128),  # 灰色
                           'olive': (128, 128, 0),  # 橄榄色
                           'purple': (128, 0, 128),  # 紫色
                           'turquoise': (64, 224, 208),  # 绿宝石色
                           'seagreen': (46, 139, 87),  # 海洋绿色
                           'cyan': (0, 255, 255),  # 青色
                           'green': (0, 128, 0),  # 纯绿色
                           'blue': (0, 0, 255),  # 纯蓝色
                           'darkblue': (0, 0, 139),  # 深蓝色
                           'navy': (0, 0, 128),  # 海军蓝色
                           'black': (0, 0, 0),  # 纯黑色
                           }

        # 元素的数字颜色
        self.NUM_COLOR_DICT = {'2': self.COLOR_DICT['gray'], '4': self.COLOR_DICT['brown'],
                               '8': self.COLOR_DICT['violet'], '16': self.COLOR_DICT['wheat'],
                               '32': self.COLOR_DICT['coral'], '64': self.COLOR_DICT['turquoise'],
                               '128': self.COLOR_DICT['navy'], '256': self.COLOR_DICT['olive'],
                               '512': self.COLOR_DICT['orange'], '1024': self.COLOR_DICT['seagreen'],
                               '2048': self.COLOR_DICT['purple']}

        self.TILE_SIZE = 80  # 设置数字元素的大小
        self.WINDOW_BLOCK_NUM = 4  # 设置行列个数