# 2. Напишите программу для проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Я так и не поняла эту задачу, что должно выводиться на экран.
# мне ее помогли решить (сказали, что вроде бы так).
# И то я не уверена, что решение верное. 
# Буду ждать разбор домашки на семинаре.

for x in [1,0]:
    for y in [1,0]:
        for z in [1,0]:
            print(x,'AND',y,'OR',z,'=',x and y or z)
