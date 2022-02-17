# def del_by(ind: int, arr: list):
#     print(arr)
#     for i in range(ind, len(arr) - 1):
#         arr[i] = arr[i + 1]
#     arr[len(arr) - 1] = 0
#     print(arr)
#
#
# # del_by(0, [1, 2, 3, 4])
# # del_by(1, [1, 2, 3, 4])
# del_by(44, [1, 2, 3, 4])


# '''
# ЗАДАНИЕ №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# '''
# # СУММА
# try:
#     num = int(input('введите число: '))
# except ValueError:
#     print('это не число')
# else:
#     sum_dig = 0
#     for i in str(num):
#         sum_dig += int(i)
#     print(sum_dig)
#
# #ПРОИЗВЕДЕНИЕ
#
# try:
#     num = int(input('введите число: '))
# except ValueError:
#     print('это не число')
# else:
#     prod_dig = 1
#     for i in str(num):
#         prod_dig *= int(i)
#     print(prod_dig)

'''Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.
# '''
#
#
#
# print(ord('а'))
# print(ord('А'))
# print('-----------------')
# print(ord('я'))
# print(ord('Я'))
#

#
# num_chr = int(input('Введите код символа: '))
#
# while num_chr < 1040 or num_chr > 1103:
#     print('Нет такого кода символа" Повторите ввод')
#     num_chr = int(input('Введите код символа: '))
# # print(f'Случайный символ с кодом {num_chr} и будет... {chr(num_chr)}')
# #
# from random import randrange
#
# custom_chr_l = input('Введите первый символ: ')
# custom_chr_r = input('Введите последний символ: ')
# new_custom_chr = randrange(ord(custom_chr_l), ord(custom_chr_r))
# print(f'Случайный символ между {custom_chr_l} и {custom_chr_r} будет... {chr(new_custom_chr)}')


print(ord('A'))
print(ord('z'))
