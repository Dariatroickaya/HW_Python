# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

a = input('Введите число: ')
n = a
n = n.replace('.', '')
n = int(n)

sum = 0
while (n != 0):
    sum = sum + n % 10
    n = n // 10
print(a, '->', sum)