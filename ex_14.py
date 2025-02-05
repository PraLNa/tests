# Удаление дубликатов из списка
# 1. функция unique_elements(lst): убирает повторы.
# 2. создание нового списка без дубликатов
#
# пример:
#
# вход:
# [1, 2, 2, 3, 4, 4, 5]
#
# выход:
#
# [1, 2, 3, 4, 5]

def unique_elements(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(key=lst.index)
    return unique_lst

input_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(input_list)
print(result)
