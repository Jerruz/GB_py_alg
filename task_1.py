def count_even_odd(num: int):
    even = 0
    odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    print(f'четных цифр - {even}, нечетных - {odd}')

count_even_odd(14562)

# Через рекурсию не работает почему-то. Не пойму, где ошибка.

def count_even_odd_rec(num2: int):
    even2 = 0
    odd2 = 0
    if num2 == 0:
        print(f'четных цифр - {even2}, нечетных - {odd2}')
    elif num2 % 2 == 0:
        even2 += 1
        num2 = num2 // 10
        return count_even_odd_rec(num2)
    else:
        odd2 += 1
        num2 = num2 // 10
        return count_even_odd_rec(num2)

count_even_odd_rec(456)