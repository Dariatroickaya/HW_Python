# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

text = [2, 3, 4, 5, 6, 7]
text2 = []

res = 0
if (len(text)) % 2 == 0:
    for i in range (int(len(text)/2)):
        res = text[i] * (text[-1]-i)
        text2.append(res)
else:
    for i in range (int(len(text)/2+1)):
        res = text[i] * (text[-1]-i)
        text2.append(res)        
print(text2)        
       