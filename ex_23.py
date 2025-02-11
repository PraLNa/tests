# Разделение строки на группы по N символов
#
# Структура задачи:
#
# 1. Получить строку и число N
# 2. Разелить строку на части и по N символов
#
# пример:
#
# вход:
# abcdefghijklm
# 3
#
# выход:
# ['abc', 'def', 'ghi', 'jkl', 'm']

def split_string_into_groups(input_string, n):
    return [input_string[i:i+n] for i in range(0, len(input_string), n)]

input_string = "abcdefghijklm"
n = 3
output = split_string_into_groups(input_string, n)
print("Вход:", input_string)
print("N:", n)
print("Выход:", output)