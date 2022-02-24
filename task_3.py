from random import randint

num = [randint(1, 100) for i in range(20)]
print(*num)
num_min = min(num)
num_max = max(num)
print('min: ', num_min)
print('max: ', num_max)
summ = sum(num[min(num.index(num_min), num.index(num_max)) + 1:max(num.index(num_min), num.index(num_max))])
print(summ)
