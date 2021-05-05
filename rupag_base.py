from rupag import Autogui
import pyautogui as pag
import sys
import os
import pandas as pd
import time
import math


def rupag_base():
    Autogui().do_start()    # 開始時のみ、連続利用時はカット
    # ↓ ↓ ↓ 以下を 自由に 書き直してください  ↓ ↓ ↓

    Autogui(interval=2, write='test menu').pbar()
    Autogui(500, 500).move()
    Autogui(500, 600).move()
    Autogui(600, 500).move()
    Autogui(600, 600).move()
    Autogui(700, 500).move()
    Autogui(700, 600).move()
    Autogui(700, 600).click()
    Autogui(path='C:\Program Files\Google\Chrome\Application\chrome.exe').do_exe()
    Autogui(interval=2).wait()
    Autogui(delaytime=30, interval=3, image='chrome.png').delay()
    Autogui(hk1='Altleft', hk2='f4').hotkey()
    Autogui(700, 600).click()
    Autogui(write='qwertyuiop ').keybord()

    # ↑ ↑ ↑ ここまで  ↑ ↑ ↑
    Autogui(end_delay=300).do_end()


if __name__ == "__main__":

    rupag_base()
