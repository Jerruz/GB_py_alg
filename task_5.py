'''
ЗАДАНИЕ №5
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько
между ними находится букв.
'''

custom_chr_1 = ord(input('Введите первую букву: '))
custom_chr_2 = ord(input('Введите вторую букву: '))
custom_chr_1 = custom_chr_1 - ord('a') + 1
custom_chr_2 = custom_chr_2 - ord('a') + 1
print(f'Позиция первого символа {custom_chr_1}, а второго {custom_chr_2}')
print('Между буквами символов:', abs(custom_chr_1-custom_chr_2)-1)


