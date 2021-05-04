from rupag import Autogui
import pyautogui as pag
import sys
import os
import pandas as pd
import time
import math


def rupag_base():

    print('')
    print('   |', 'Python    : ', sys.version)
    print('   |', 'PyAutoGUI : ', pag.__version__)
    print('')

    start = time.time()

    # ↓ ↓ ↓ 以下を 自由に 書き直してください ↓ ↓ ↓

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

    # ↑ ↑ ↑ ここまで ↑ ↑ ↑

    print('')
    print('Total time :', round(time.time()-start, 2), 'sec')
    print('Hold the result for 5 minutes...   - Press "Ctrl + C" to exit. -')
    print('')
    time.sleep(300)


if __name__ == "__main__":

    rupag_base()
