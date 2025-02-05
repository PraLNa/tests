# Проверка палиндрома
# 1. Функция is_palindrome(lst): проверяет, равен ли список самому себе задом
#
# пример:
#
# вход:
# [1, 2, 3, 2, 1]
#
# выход:
# True

def is_palindrome(lst):
    return lst == lst[::-1]

example_list = [1, 2, 3, 2, 1]
result = is_palindrome(example_list)
print(result)
