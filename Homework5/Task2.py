# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход 
# друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты 
# у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

move = 0
candy = 2021
min = 1
max = 28

n = int(input('Введите число игроков (1 или 2): '))
player = random.randint(1, 2)
while candy > 0:
    if player == 1:
        player = 2
    else:
        player = 1
    move += 1
    if n == 1 and player == 2:
        print(move, 'ход: всего', candy, 'конфет', end = ' ')
        if candy <= max:
            c = candy
        else:
            c = random.randint(1, 28)
        print('Компьютер забирает:', c)
        candy -= c
    else:
        print(move, 'ход: всего', candy, 'конфет. Игрок', player, end = ' ')
        c = int(input('забирает: '))
        if c < min:
            print('Внимание! Нельзя пропускать ход, Игрок', player, 'взял', min, 'конфету')
            c = min
        elif c > candy and candy <= max:
            print('Внимание! Столько конфет нет, Игрок', player, 'взял только', candy, 'конфет')
            c = candy
        elif c > max:
            print('Внимание! Столько конфет нельзя брать за 1 ход, Игрок', player, 'взял только', max, 'конфет')
            c = max
        candy -= c
if n == 1 and player == 2:
    print('Победа! Компьютер победил за', move, 'ходов и забирает все конфеты.')
else:
    print('Победа! Игрок', player, 'победил за', move, 'ходов и забират все конфеты.') 