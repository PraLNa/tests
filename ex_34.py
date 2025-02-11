# Поиск всех подстрок в строке
#
# структура задачи:
#
# 1. Получить строку
# 2. Найти все возможные подстроки
#
# пример:
#
# вход:
# abc
#
# выход:
# ['a', 'b', 'c', 'ab', 'bc', 'abc']

def find_all_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])

    return substrings

input_string = input("Введите строку: ")
result = find_all_substrings(input_string)
print(result)
