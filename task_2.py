from random import randint

num = [randint(-50, 50) for ff in range(randint(1, 20))]
print(num)
i_max, i_min = num.index(max(num)), num.index(min(num))
num[i_max], num[i_min] = num[i_min], num[i_max]
print(num)
