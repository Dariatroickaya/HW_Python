# Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число больше ноля: '))
lst = []

res = 0
for i in range(1, n+1):
    res = (1 + 1/i)**i
    lst.append(res)

sum = 0
for j in range(len(lst)):
    sum += lst[j]
print(n, '->', sum)