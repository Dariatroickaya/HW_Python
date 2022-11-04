# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

#  Пример:


# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]
# (https://ru.wikipedia.org/wiki/Негафибоначчи#:~:text=В математике%2C числа негафибоначчи — отрицательно индексированные элементы последовательности чисел Фибоначчи.)


n = int(input('Введите число: '))

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)    
     
lst1 = []
for e in range(1, n+1):
    lst1.append(fib(e))
   

def negfib(n):
    if n in [1, 2]:
        return 1
    else:
        return negfib(n+2) - negfib(n+1)    
  
lst2 = []
for e in range(0, (-n)-1, -1):
    lst2.append(negfib(e))

print((list(reversed(lst2)))+lst1)