# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
list = []

import random
for i in range(n):
    list.append(random.randint(-n, n)) 
print(list)

list2 = []
with open('file.txt', 'r') as file:
    for line in file:
        if int(line) < len(list):
            list2.append(list[int(line)])
print(list2)

res = 1
for j in range(len(list2)):
    res = (res * list2[j])
    j += 1
print(res)