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
        print('%20s' % ('Pointer Move |'), f'{self.x, self.y}')
        time.sleep(self.interval)
        pag.moveTo(self.x, self.y, duration=self.duration)

    # マウス・クリック
    def click(self):
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
            time.sleep(1)
        pag.moveTo(c_x, c_y-150, duration=0.05)

    # ディレイ・画像反応待ち（グルグル参照）
    def delay(self):
        print('%20s' % ('Delay/Image |'), self.delaytime,
              'sec :', 'images/' + self.image)
        pos = None
        start = time.time()
        while time.time()-start <= self.delaytime:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=0.3)
            if pos is None:
                self.wait(fromdelay=1)
                continue
            break
        if pos is None:
            # print('Not Found...')    ####
            quit()

    # ディレイ・プログレッシブバー
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


if __name__ == "__main__":

    # class 実施例
    gui0 = Autogui(interval=1)
    gui1 = Autogui(500, 500)
    gui2 = Autogui(500, 600)
    gui3 = Autogui(600, 500)
    gui4 = Autogui(600, 600)
    gui5 = Autogui(700, 500)
    gui6 = Autogui(700, 600)
    gui7 = Autogui(700, 600)
    gui8 = Autogui(
        path='C:\Program Files\Google\Chrome\Application\chrome.exe')
    gui9 = Autogui(interval=3)
    gui13 = Autogui(delaytime=30, interval=3, image='chrome.png')
    gui10 = Autogui(hk1='Altleft', hk2='f4')
    gui11 = Autogui(700, 600)
    gui12 = Autogui(write='qwertyuiop')

    start = time.time()

    gui0.pbar()
    gui1.move()
    gui2.move()
    gui3.move()
    gui4.move()
    gui5.move()
    gui6.move()
    gui7.click()
    gui8.do_exe()
    gui9.wait()
    gui13.delay()
    gui10.hotkey()
    gui11.click()
    gui12.keybord()

    print('')
    print('Total time :', round(time.time()-start, 2), 'sec')
    print('')

    # CSV input 実施例
    print('input arg :', sys.argv[1])
    intable = pd.read_csv('input_table/' + sys.argv[1], index_col=0)
    start = time.time()

    for i in intable.index:

        in_func = intable.iloc[i, 0]
        in_arg = intable.iloc[i, 1:]

        if i == 0:
            old_arg = in_arg.to_list()

        # str の引数は エラー回避のため 毎回 再str化しておく
        in_arg = [str(in_arg[k]) if (k in [4, 5, 6, 7, 8, 9, 10])
                  == True else in_arg[k] for k in range(len(in_arg))]

        # str 以外の引数で nan の場合は 前の引数を参照する
        for j in range(len(in_arg)):
            if (j in [4, 5, 6, 7, 8, 9, 10]) == False:
                in_arg[j] = old_arg[j] if math.isnan(
                    in_arg[j]) == True else in_arg[j]

        old_arg = in_arg
        if i == 0:
            continue

        gui = Autogui(*in_arg)

        if in_func == 'move':
            gui.move()
        if in_func == 'click':
            gui.click()
        if in_func == 'keybord':
            gui.keybord()
        if in_func == 'hotkey':
            gui.hotkey()
        if in_func == 'do_exe':
            gui.do_exe()
        if in_func == 'wait':
            gui.wait()
        if in_func == 'delay':
            gui.delay()
        if in_func == 'pbar':
            gui.pbar()

    print('')
    print('Total time :', round(time.time()-start, 2), 'sec')
    print('')
