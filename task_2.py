'''
ЗАДАНИЕ №2
Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
'''

# Бинарное И

var_and = 5 & 6
print(var_and)

# Бинарное ИЛИ

var_or = 5 | 6
print(var_or)

# Бинарное ИЛИ НЕТ

var_or_not = 5 ^ 6
print(var_or_not)

# Бинарный сдвиг влево на 2 знака

var_l = 5 << 2
print(var_l)

# Бинарный сдвиг вправо на 2 знака

var_r = 5 >> 2
print(var_r)

