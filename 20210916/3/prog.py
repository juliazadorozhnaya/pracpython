import random
a = eval(input())
i = 0
while i < 9:
    x = random.randint(1, 100)
    a.append(x)
    i += 1
print(a)
