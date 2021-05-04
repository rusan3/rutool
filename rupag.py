import pyautogui as pag
import numpy as np
import time
import os
import sys
import subprocess
import datetime
import calendar
import pandas as pd
import math
import platform


class Autogui:
    '''
    "自動化機能まとめ"

    '''

    # 初期化
    def __init__(self, x=100, y=100, duration=0.2, interval=0.2,
                 write='', hk1='', hk2='', hk3='', hk4='', path='',
                 image='', delaytime=120):
        self.x = x
        self.y = y
        self.duration = duration
        self.interval = interval
        self.write = write
        self.hk1 = hk1
        self.hk2 = hk2
        self.hk3 = hk3
        self.hk4 = hk4
        self.path = path
        self.image = image
        self.delaytime = delaytime

    # マウス・移動
    def move(self):
        try:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=0.75)
            self.x, self.y = pag.center(pos)
            print('%20s' % ('Pointer Move |'),
                  f'{self.x, self.y},', 'images/' + self.image)
        except:
            print('%20s' % ('Pointer Move |'), f'{self.x, self.y}')
        time.sleep(self.interval)
        pag.moveTo(self.x, self.y, duration=self.duration)

    # マウス・左クリック
    def click(self):
        try:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=0.75)
            self.x, self.y = pag.center(pos)
            print('%20s' % ('Click Left |'),
                  f'{self.x, self.y},', 'images/' + self.image)
        except:
            print('%20s' % ('Click Left |'), f'{self.x, self.y}')
        time.sleep(self.interval)
        pag.click(self.x, self.y, duration=self.duration)

    # キーボード・入力（単独押し）
    def keybord(self):
        print('%20s' % ('Keybord |'), f'{self.write}')
        time.sleep(self.interval)
        pag.typewrite(self.write, 0.005)

    # キーボード・ホットキー（同時押し）
    def hotkey(self):
        print('%20s' % ('Hotkey 1to4 |'),
              f'{self.hk1},', f'{self.hk2},' f'{self.hk3},', f'{self.hk4}')
        time.sleep(self.interval)
        pag.hotkey(self.hk1, self.hk2, self.hk3, self.hk4)

    # アプリケーション実行
    def do_exe(self):
        print('%20s' % ('Path |'), f'{self.path}')
        runroop = subprocess.Popen(f"{self.path}", shell=True)

    # ディレイ・一定時間マウスグルグル
    def wait(self, fromdelay=0):
        if fromdelay == 0:
            print('%20s' % ('Wait |'), self.interval, 'sec')
        r, fai, delta, lr, frequency = (150, -90, 45, 1, 0.1)    # 固定
        c_x, c_y = (400, 300)      # サークル中心 X･Y
        start = time.time()
        while time.time()-start <= self.interval:
            for i in range(2*int(360/delta)+1):
                pag.moveTo(r*math.cos(math.radians(fai+delta*i*lr))+c_x,
                           r*math.sin(math.radians(fai+delta*i*lr))+c_y,
                           duration=0.05)
                if time.time()-start >= self.interval:
                    break
            time.sleep(0.5)

    # ディレイ・画像反応待ち（グルグル参照）
    def delay(self):
        print('%20s' % ('Delay/Image |'), self.delaytime,
              'sec :', 'images/' + self.image, end=' ')
        pos = None
        start = time.time()
        while time.time()-start <= self.delaytime:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=0.75)
            if pos is None:
                self.wait(fromdelay=1)
                continue
            print('==>> OK! ', round(time.time()-start, 2), 'sec')
            break
        if pos is None:
            print('==>> Not Found... Quit')
            quit()

    # ディレイ・プログレスバー
    def pbar(self):
        for i in range(0, 10):
            if i != 9:
                pro_bar1 = ('===' * (i)) + '==>'
            else:
                pro_bar1 = ('===' * (i+1))
            pro_bar2 = (' - '*(10-(i+1)))
            print('\r   [%s%s] %3d /%3d sec  ' % (pro_bar1, pro_bar2,
                                                  int((i+1)*(self.interval/10)),
                                                  self.interval), end='')
            time.sleep(self.interval/10)
        print('')
        print('%20s' % ('Progress Bar |'), f'{self.write}')


def rupag():

    print('')
    print('   |', 'Python    : ', sys.version)
    print('   |', 'PyAutoGUI : ', pag.__version__)
    print('')

    # class 実施例
    start = time.time()

    gui = Autogui(interval=2, write='test menu').pbar()
    gui = Autogui(500, 500).move()
    gui = Autogui(500, 600).move()
    gui = Autogui(600, 500).move()
    gui = Autogui(600, 600).move()
    gui = Autogui(700, 500).move()
    gui = Autogui(700, 600).move()
    gui = Autogui(700, 600).click()
    gui = Autogui(
        path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    gui = Autogui(interval=2).wait()
    gui = Autogui(delaytime=30, interval=3, image='chrome.png').delay()
    gui = Autogui(hk1='Altleft', hk2='f4').hotkey()
    gui = Autogui(700, 600).click()
    gui = Autogui(write='qwertyuiop').keybord()

    print('')
    print('Total time :', round(time.time()-start, 2), 'sec')
    print('')


def demo1():

    print('')
    print('   |', 'Python    : ', sys.version)
    print('   |', 'PyAutoGUI : ', pag.__version__)
    print('')

    gui = Autogui(interval=2, write='test menu').pbar()
    gui = Autogui(500, 500, image='chrome.png').move()
    gui = Autogui(500, 500, image='chrome.png').click()


if __name__ == "__main__":

    rupag()
    # demo1()
