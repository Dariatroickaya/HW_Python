# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#  Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

a = int(input('Введите число: '))
lst = []
n = a
while(n >= 1):
    res = n % 2
    n /= 2
    lst.append(int(res))

print(a, '->', int(''.join(map(str, list(reversed(lst))))))