'''
ЗАДАНИЕ №1
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
'''

# СУММА
try:
    num = int(input('введите число: ')) # не додумался, как оставить проверку на число и избавиться от первых int и str
except ValueError:
    print('это не число')
else:
    sum_dig = 0
    for i in str(num):
        sum_dig += int(i)
    print(sum_dig)

# ПРОИЗВЕДЕНИЕ

try:
    num = int(input('введите число: ')) # не додумался, как оставить проверку на число и избавиться от первых int и str
except ValueError:
    print('это не число')
else:
    prod_dig = 1
    for i in str(num):
        prod_dig *= int(i)
    print(prod_dig)
