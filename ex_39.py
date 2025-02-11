# Разбиение списка на N частей
#
# структура задачи:
#
# 1. Получить список и число N
# 2. Разделить список на N частей
#
# пример:
#
# вход:
# [1, 2, 3, 4, 5, 6], 3
#
# выход:
# [[1, 2], [3, 4], [5, 6]]

def split_list(input_list, n):
    k, m = divmod(len(input_list), n)
    return [input_list[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

input_list = [1, 2, 3, 4, 5, 6]
n = 3
result = split_list(input_list, n)

print(result)
