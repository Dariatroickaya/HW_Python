# 2. Напишите программу для проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



# ВАРИАНТ 1

for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            print('Истина' if not (x or y or z) == (not x and not y and not z) else 'Ложь')


# ВАРИАНТ 2            

for x in [1,0]:
    for y in [1,0]:
        for z in [1,0]:
            print(x, y, z)
            print('Истина' if not (x or y or z) == (not x and not y and not z) else 'Ложь')



# ВАРИАНТ 3

s = range(2)
res = True

for x in s:
    for y in s:
        for z in s:
            if not (not (x or y or z) == (not x and not y and not z)):
                res = False
                break
print(res) 



## ВАРИАНТ 4 
print(*[f'x = {x}, y = {y}, z = {z} = Утверждение верно' if not (x or y or z) == (not x and not y and not z) else 'Утверждение не верно' for z in range(2) for y in range(2) for x in range(2)], sep = '\n')  



## ВАРИАНТ 5 
print(*(not (x or y or z) == (not x and not y and not z) for z in range(2) for y in range(2) for x in range(2)), sep = '\n')  



## ВАРИАНТ 6 

from itertools import product
print(all(not (x or y or z) == (not x and not y and not z) for x, y, z in product (*((True, False),)*3,)))