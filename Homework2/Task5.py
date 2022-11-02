# Реализуйте алгоритм перемешивания списка.

import random

lst = []
for i in range(10):
    lst.append(random.randint(0, 9)) 
print(lst)

random.shuffle(lst)
print(lst) 