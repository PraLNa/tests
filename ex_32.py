# объединение двух списков без повторяющихся элементов
#
# структура задачи:
#
# 1. Получить два списка
# 2. Объединить  их, убирая дубликаты
#
# пример:
#
# вход:
# [1, 2, 3], [3, 4, 5]
#
# выход:
# [1, 2, 3, 4, 5]

def merge_lists(list1, list2):
    merged_set = set(list1) | set(list2)
    merged_list = list(merged_set)
    return merged_list

list1 = [1, 2, 3]
list2 = [3, 4, 5]
result = merge_lists(list1, list2)
print(result)
