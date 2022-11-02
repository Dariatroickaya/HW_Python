# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
lst = []

import random
for i in range(n):
    lst.append(random.randint(-n, n)) 
print(lst)

lst2 = []
with open('file.txt', 'r') as file:
    for line in file:
        if int(line) < len(lst):
            lst2.append(lst[int(line)])
print(lst2)

res = 1
for j in range(len(lst2)):
    res = (res * lst2[j])
print(res)