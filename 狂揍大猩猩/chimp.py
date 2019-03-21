#用拳头击打黑猩猩

import os, pygame
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0] # 获取python文件所在路径
data_dir = os.path.join(main_dir, 'data')  # 获取data文件夹路径

def load_image(name, colorkey=None):  # 加载图片的方法
    fullname = os.path.join(data_dir, name)  # 拼接图片路径
    image = pygame.image.load(fullname) # 加载图片
    image = image.convert()  # 透明化
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL) 
    return image, image.get_rect()   # 返回图片和图片矩形信息

def load_sound(name):  # 加载声音的方法
    fullname = os.path.join(data_dir, name) # 拼接声音文件的路径
    sound = pygame.mixer.Sound(fullname) # 获取声音文件的路径
    return sound  #返回声音


class Fist(pygame.sprite.Sprite): # 按下鼠标，握紧拳头
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('fist.bmp', -1)  # 获取图片与矩形
        self.punching = 0  # 用于是否击打

    def update(self):  #基于鼠标位置，移动拳头
        pos = pygame.mouse.get_pos()  # 获取鼠标位置
        self.rect.midtop = pos  # 设置拳头的位置
        if self.punching:
            self.rect.move_ip(5, 10)

    def punch(self, target):
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self): # 拉回拳头
        self.punching = 0


class Chimp(pygame.sprite.Sprite):  # 大猩猩 ，被击打时可以旋转
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.image, self.rect = load_image('chimp.bmp', -1) # 加载图片
        screen = pygame.display.get_surface() #得到表明
        self.area = screen.get_rect()  #表面矩形区域
        self.rect.topleft = 10, 10  #设置矩形左上顶点的位置
        self.move = 9  # 移动速度
        self.dizzy = 0 # 角度

    def update(self):
        if self.dizzy:
            self._spin()  # 旋转
        else: 
            self._walk()  # 行走

    def _walk(self):  # 移动的方法
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or self.rect.right > self.area.right: # 判断是否碰到左右边缘
            self.move = -self.move # 速度反向
            newpos = self.rect.move((self.move, 0)) # 移动大猩猩
            self.image = pygame.transform.flip(self.image, 1, 0)  # 旋转
        self.rect = newpos # 重新设定矩形框的位置

    def _spin(self): # 旋转大猩猩的方法
        center = self.rect.center 
        self.dizzy = self.dizzy + 12  # 每隔12度旋转一次
        if self.dizzy >= 360:  # 度数大于360度时
            self.dizzy = 0     # 重新设置度数为0
            self.image = self.original # 获取原始图片
        else:
            self.image = pygame.transform.rotate(self.original, self.dizzy) # 否则旋转
        self.rect = self.image.get_rect(center=center) # 获得矩形

    def punched(self): # 引起大猩猩旋转的方法
        if not self.dizzy:  # 如果dizzy==0
            self.dizzy = 1  # 设置dizzy
            self.original = self.image # 设置原始图片

def main():
    pygame.init() # 初始化
    screen = pygame.display.set_mode((468, 60))  # 生成窗口
    pygame.display.set_caption('Monkey Fever')   # 设置窗口的标题
    pygame.mouse.set_visible(0)  # 设置鼠标不可见

    background = pygame.Surface(screen.get_size()) #获取窗口背景
    background = background.convert()  # 转换成透明
    background.fill((250, 250, 250))   # 填充白色
    if pygame.font:
        font = pygame.font.Font(None, 36)  # 生成字体样式
        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10)) # 渲染字体
        textpos = text.get_rect(centerx=background.get_width()/2) 
        background.blit(text, textpos) # 输出字体
    screen.blit(background, (0, 0))  #输出背景到窗口
    pygame.display.flip()  # 刷新

    clock = pygame.time.Clock()  # 设定时钟
    whiff_sound = load_sound('whiff.wav')  # 加载声音
    punch_sound = load_sound('punch.wav')  # 加载声音
    chimp = Chimp() # 生成chimp
    fist = Fist()   # 生成fist
    allsprites = pygame.sprite.RenderPlain((fist, chimp))
    going = True
    while going:
        clock.tick(60)  # 每秒循环60次
        for event in pygame.event.get():
            if event.type == QUIT: # 处理退出事件
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:  # 处理退出事件
                going = False
            elif event.type == MOUSEBUTTONDOWN:  # 鼠标按下事件
                if fist.punch(chimp):
                    punch_sound.play() #播放声音
                    chimp.punched()
                else:
                    whiff_sound.play() #miss
            elif event.type == MOUSEBUTTONUP:  #松开鼠标事件
                fist.unpunch()

        allsprites.update()  # 更新精灵
        screen.blit(background, (0, 0))  # 画背景表面于窗口
        allsprites.draw(screen)          # 画所有精灵于窗口
        pygame.display.flip()            # 刷新

    pygame.quit()

if __name__ == '__main__':
    main()
