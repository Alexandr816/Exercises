from random import choice
'''Лотерея. Могут выпасть четыре случайных числа или буквы из списка'''
my_list = (1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e')

def win(my_list=my_list):
    combination = [choice(my_list) for i in range(4)]
    return combination

print(f'В этот раз выиграл билет с комбинацией: {win()}')
