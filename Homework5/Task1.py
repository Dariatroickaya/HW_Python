# Напишите программу, удаляющую из текста все слова, 
# в которых присутствуют все буквы "абв".

lst = ['абвгдейка', 'обвал', 'вобла', 'болван', 'трагедия', 'собака', 'кизил', 'изюм']
lst2 = set('абв')
print(lst, [i for i in lst if not lst2 <= set(i)], sep = '\n')  