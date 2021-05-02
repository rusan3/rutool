from rupag import Autogui
import sys
import pandas as pd
import time
import math


if __name__ == "__main__":

    # CSV input 実施例
    print('input arg :', sys.argv[1])
    intable = pd.read_csv('input_table/'+sys.argv[1], index_col=0)
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
