from exe9_14 import win
'''Показывает сколько раз нужно повторить цикл, для получения выигрышной комбинации'''
def how_win(my_combination=win()):
    x = 1
    while True:
        play = win()
        if play == my_combination:
            print(f'you should play {x} times')
            break
        else:
            x += 1
    return x

how_win()
how_win([1,2,0,'d'])

