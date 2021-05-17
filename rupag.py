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
import platform    # 使用していない？
import threading
from multiprocessing import Process


class Autogui:
    '''
    "自動化機能まとめ"

    '''

    # 初期化
    def __init__(self, x=100, y=100, duration=0.2, interval=0.2, write='',
                 key1='', key2='', key3='', key4='', path='', image='', delaytime=120,
                 start_time=time.time(), end_delay=0, confidence=0.75, posnone=1):
        self.x = x
        self.y = y
        self.duration = duration
        self.interval = interval
        self.write = write
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4
        self.path = path
        self.image = image
        self.delaytime = delaytime
        self.start_time = start_time
        self.end_delay = end_delay
        self.confidence = confidence
        self.posnone = posnone

    # 開始定例文
    def do_start(self):
        print('\n   |', 'Python    : ', sys.version)
        print('   |', 'PyAutoGUI : ', pag.__version__, end='\n\n')
        start_time = time.time()

    # 終了定例文
    def do_end(self):
        print('\n   |', 'Total time :', round(
            time.time()-self.start_time, 2), 'sec')
        if self.end_delay != 0:
            print('   |',
                  f'Hold the result for {self.end_delay} seconds...   - Press "Ctrl + C" to exit. -', end='\n\n')
        time.sleep(self.end_delay)

    # マウス・移動
    def move(self):
        try:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=self.confidence)
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
                                     grayscale=True, confidence=self.confidence)
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
        print('%20s' % ('Hotkey |'), end='')
        if self.key4 == '':
            if self.key3 == '':
                print(f' {self.key1} + {self.key2}', end=' \n')
            else:
                print(f' {self.key1} + {self.key2} + {self.key3}', end=' \n')
        else:
            print(
                f' {self.key1} + {self.key2} + {self.key3} + {self.key4}', end=' \n')
        time.sleep(self.interval)
        pag.hotkey(self.key1, self.key2, self.key3, self.key4)

    # キーボード・Keyhold継続（キー押しながら別キー）
    def holdkey(self):
        sltime = 0.1
        print('%20s' % ('Hold Key |'), end='')
        time.sleep(self.interval)
        if self.key4 == '':
            if self.key3 == '':
                print(f' {self.key1} + ( {self.key2}', end=' )\n')
                pag.keyDown(self.key1)
                time.sleep(sltime)
                pag.press(self.key2)
                time.sleep(sltime)
                pag.keyUp(self.key1)
            else:
                print(f' {self.key1} + ( {self.key2}, {self.key3}', end=' )\n')
                pag.keyDown(self.key1)
                time.sleep(sltime)
                pag.press(self.key2)
                time.sleep(sltime)
                pag.press(self.key3)
                time.sleep(sltime)
                pag.keyUp(self.key1)
        else:
            print(
                f' {self.key1} + ( {self.key2}, {self.key3}, {self.key4}', end=' )\n')
            pag.keyDown(self.key1)
            time.sleep(sltime)
            pag.press(self.key2)
            time.sleep(sltime)
            pag.press(self.key3)
            time.sleep(sltime)
            pag.press(self.key4)
            time.sleep(sltime)
            pag.keyUp(self.key1)

    # キーボード・キーダウン（holdkey では足りない場合は 解除まで keydown）
    def keydown(self):
        print('%20s' % ('Key Down |'), f'{self.key1}')
        time.sleep(self.interval)
        pag.keyDown(self.key1)

    # キーボード・キーアップ（keydown と 併用する）
    def keyup(self):
        print('%20s' % ('Key Up |'), f'{self.key1}')
        time.sleep(self.interval)
        pag.keyUp(self.key1)

    # キーボード・キーアップ（keydown/keyup と 併用する）
    def press(self):
        print('%20s' % ('Press |'), f'{self.key1}')
        time.sleep(self.interval)
        pag.press(self.key1)

    # アプリケーション実行
    def do_exe(self):
        print('%20s' % ('Path |'), f'{self.path}')
        subprocess.Popen(f"{self.path}", shell=True)

    # ディレイ・一定時間マウスグルグル
    def sleep(self):
        print('%20s' % ('Sleep |'), self.interval, 'sec')
        time.sleep(self.interval)

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
            time.sleep(2)

    # ディレイ・画像反応待ち（グルグル参照）
    def delay(self):
        print('%20s' % ('Delay/Image |'), self.delaytime,
              'sec :', 'images/' + self.image, end=' ')
        pos = None
        start = time.time()
        while time.time()-start <= self.delaytime:
            pos = pag.locateOnScreen('images/'+self.image,
                                     grayscale=True, confidence=self.confidence)
            if pos is None:
                self.wait(fromdelay=1)
                continue
            break
        if pos is None:
            if self.posnone == 0:       # 0 : 完全停止
                print('==>> Not Found... Quit')
                quit()
            elif self.posnone == 1:     # 1 : その処理(関数)中止
                print('==>> Not Found... Return!!')
                return
            elif self.posnone == 2:     # 2 : ディレイ後続行
                print('==>> End of Delay Time...',
                      round(time.time()-start, 2), 'sec')
            else:                       # その他 : 完全停止
                print('==>> Not Found... Quit')
                quit()
        else:
            print('==>> OK! ', round(time.time()-start, 2), 'sec')

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
        print('\n%20s' % ('Progress Bar |'), f'{self.write}')

    def judge(self):
        f_zaitaku = 0
        ipconfig = subprocess.check_output(
            "ipconfig", shell=True).decode('cp932')
        ipconfig = ipconfig[:ipconfig.find('Wireless LAN adapter Wi-Fi:')]
        if ipconfig.find('jpn.mds.honda.com') >= 0:
            if ipconfig.find('PPP アダプター GYRO VPN') >= 0:
                print('   |', "I'm telecommute now.", end='\n\n')
                f_zaitaku = 1
            else:
                print('   |', "I'm in the office, unfortunately.", end='\n\n')
        else:
            print('   |', "I'm telecommute now.", end='\n\n')
            f_zaitaku = 1
        return f_zaitaku


# 2thread 並行起動
def thread2(thre1, thre2):
    th1 = threading.Thread(target=thre1)
    th2 = threading.Thread(target=thre2)
    th1.start()
    th2.start()


# 2process 並列処理
def process2(proc1, proc2, interval):
    def process2_wait(interval):
        Autogui(interval).wait()
        # Autogui(delaytime=30, interval=3, image='chrome.png').delay()
    pr1 = Process(target=proc1)
    pr2 = Process(target=proc2)
    pr2.start()
    pr1.start()
    process2_wait(interval)


def rupag():
    # class 実施例
    zai = Autogui().judge()
    if zai == 1:
        return
    Autogui(interval=2, write='test menu').pbar()
    Autogui(500, 500).move()
    Autogui(500, 600).move()
    Autogui(600, 500).move()
    Autogui(600, 600).move()
    Autogui(700, 500).move()
    Autogui(700, 600).move()
    Autogui(700, 600).click()

    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(interval=2).wait()
    Autogui(delaytime=30, interval=3, image='chrome.png').delay()
    Autogui(key1='Altleft', key2='f4', key3='f4', key4='f4').holdkey()

    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=0.2).sleep()
    Autogui(interval=2).wait()
    Autogui(delaytime=30, interval=3, image='chrome.png').delay()
    Autogui(key1='Altleft').keydown()
    Autogui(interval=0.2).sleep()
    Autogui(key1='f4').press()
    Autogui(interval=0.2).sleep()
    Autogui(key1='f4').press()
    Autogui(interval=0.2).sleep()
    Autogui(key1='f4').press()
    Autogui(interval=0.2).sleep()
    Autogui(key1='Altleft').keyup()
    Autogui(700, 600).click()
    Autogui(write='qwertyuiop ').keybord()


if __name__ == "__main__":

    Autogui().do_start()

    # ↓ ↓ ↓ 以下を 自由に 書き直してください  ↓ ↓ ↓
    rupag()
    # ↑ ↑ ↑ ここまで                        ↑ ↑ ↑

    Autogui(end_delay=300).do_end()
