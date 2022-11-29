# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности, список повторяемых и убрать дубликаты 
# из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

lst = [1, 2, 3, 5, 1, 5, 3, 10]

# список уникальных элементов: 

# lst2 = []
# for i in lst:
#     if lst.count(i) == 1:
#         lst2.append(i)

lst2 = [i for i in lst if lst.count(i) == 1]
print(lst2)    


# список повторяемых элементов:

# lst2 = []
# for i in lst:
#     if lst.count(i) != 1:
#         lst2.append(i)
# lst2 = set(lst2)        
# lst2 = list(lst2)

lst2 = [i for i in lst if lst.count(i) != 1]
print(list(set(lst2)))    



# убрать дубликаты: 

# lst = set(lst)
# lst = list(lst)
# print(lst)

print(list(set(lst)))
