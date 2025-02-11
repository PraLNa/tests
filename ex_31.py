# Проверка, является ли строка палиндромом
#
# Структура задачи:
#
# 1. Получить строку
# 2. Проверить, является ли она палиндромом
#
# прмиер:
#
# вход:
# madam
#
# выход:
#  True

def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

input_string = input("Введите строку: ")
result = is_palindrome(input_string)
print(result)
