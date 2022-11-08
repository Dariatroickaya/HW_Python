# 1) Вычислить число c заданной точностью d

# Пример:
# при d = 0.001, π = 3.142  
# 10^(-1) ≤ d ≤10^(-10)

import random

n = random.uniform(1, 9)
print(n)

degree = random.randint(-10, -1)
d = 10 ** degree
print(d)

print(round(n, -degree))