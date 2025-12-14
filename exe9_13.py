from random import choice

class Die:
    '''Класс имитирует кубик(кости)'''
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        '''Бросок кубика'''
        sides_die = [side for side in range(1,self.sides+1)]
        roll = choice(sides_die)
        return roll

my_play = Die()
#for i in (range(10)):
#    print(my_play.roll_die())

'''Бросок кубика с разным количеством граней'''
for i in [my_play.sides,10,16,20]:
    my_play.sides = i
    print(f'\nsides_die = {i}\n')
    for i in (range(10)):
        print(my_play.roll_die())

