from random import randint

num = [randint(1, 100) for i in range(20)]
print(*num)
print(*sorted(num)[:2])
