from math import factorial

s = 0
for i in range(3, 100000):
    if i == sum(map(factorial, map(int, str(i)))):
        s += i

print(s)
