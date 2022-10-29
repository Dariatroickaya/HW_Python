# Реализуйте алгоритм перемешивания списка.

import random

list = []
for i in range(10):
    list.append(random.randint(0, 9)) 
print(list)

random.shuffle(list)
print(list) 