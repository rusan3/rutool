import pyautogui as pag
import time
import os
import subprocess
import datetime
import calendar
import pandas as pd
import math


# プログレッシブバー
def pbar(t_sleep, pbartext):
    sitp = t_sleep / 10
    for itp in range(0, 10):
        if itp != 9:
            pro_bar1 = ('===' * (itp)) + '==>'
        else:
            pro_bar1 = ('===' * (itp+1))
        pro_bar2 = (' - '*(10-(itp+1)))
        print('\r   [%s%s] %3d /%3d sec  |  ' %
              (pro_bar1, pro_bar2, int((itp+1)*sitp), t_sleep), end='')
        time.sleep(sitp)
    print(pbartext)


# Active実行
def pa_active():

    scname = os.path.basename(__file__)

    try:
        t_limit = int(scname[scname.rfind('_') +
                             1:scname.rfind('.py')])    # 何秒間実行するか
    except:
        t_limit = 30

    t1 = 0             # 開始時間定義、変える必要なし
    acttime = 240
    acttime2 = acttime

    print('')
    print('   ---   Waiting for "Active" to be executed.   ---')
    pbar(1, '        "Active" - execute - ')
    print()

    n = 1
    t1s = time.time()
    t2s = time.time()
    xs, ys = pag.size()
    t1p = 0

    try:
        while t1 <= t_limit:

            t1e = time.time()
            t1 = round(t1e - t1s, 1)
            t2 = round(t1e - t2s, 1)

            # TODO: マウス座標を取得して表示する
            xz, yz = pag.position()
            position_str = '      No. ' + str(n) + '   |   ' + str(t1) + ' / ' + str(acttime2) + ' / ' + str(
                t_limit) + ' sec   |   X: ' + str(xz).rjust(4) + '  Y: ' + str(yz).rjust(4) + '  |  '

            print(position_str, end='')
            print('\b' * len(position_str), end='', flush=True)

            if t2 >= acttime:
                x0, y0 = pag.position()
                # pag.moveTo(xs / 2, ys / 2, duration=0.001)
                # pag.moveTo(x0, y0, duration=0.001)
                pag.typewrite(['ctrlleft'], 0.001)
                t2s = time.time()
                n += 1
                t1 = round(t1e - t1s, 1)
                # acttime2 = t1 + acttime
                acttime2 += t1 - acttime2 + acttime
                t1p = t1 - t1p
                print()

    except KeyboardInterrupt:
        print('')
        print('\n    KeyboardInterrupt')


if __name__ == "__main__":

    pa_active()
