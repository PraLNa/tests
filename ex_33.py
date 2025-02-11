# Разбиение числа на цифры
#
# Структура задачи:
#
# 1. Получить число
# 2. Разбить его на список цифр
#
# пример:
#
# вход:
# 12345
#
# выход:
# [1, 2, 3, 4, 5]

def split_number_into_digits(number):
    return [int(digit) for digit in str(number)]

input_number = input("Введите число: ")
result = split_number_into_digits(input_number)

print(result)
