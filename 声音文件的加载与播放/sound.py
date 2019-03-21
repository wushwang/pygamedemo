#!/usr/bin/env python

"""声音演示文件"""

import os.path, sys
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time

main_dir = os.path.split(os.path.abspath(__file__))[0]
print(main_dir)
def main(file_path=None):
    if file_path is None:
        file_path = os.path.join(main_dir, 'data', 'secosmic_lo.wav')   # 获取声音文件的路径

    mixer.init(11025) # 初始化声道
    sound = mixer.Sound(file_path) # 加载声音

    print ('Playing Sound...')  
    channel = sound.play()  # 播放声音文件

    while channel.get_busy():  # 直到播放完毕才结束
        print ('  ...still going...')
        time.wait(1000)
    print ('...Finished') 

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])  # 用于接收命令行参数
    else:
        main()
