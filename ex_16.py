# Чередование элементов двух списков
# 1. Функция alternate_merge(lst1, lst2): чередует элементы
# 2. Проход по минимальной длине списка
# 3. Добавление оставшихся элементов
#
# пример:
#
# вход:
# [1, 2, 3], ["a", "b", "c", "d"]
#
# выход:
# [1, "a", 2, "b", 3, "c", "d"]

def alternate_merge(lst1, lst2):
    min_length = min(len(lst1), len(lst2))

    merged_list = []

    for i in range(min_length):
        merged_list.append(lst1[i])
        merged_list.append(lst2[i])

    if len(lst1) > min_length:
        merged_list.extend(lst1[min_length:])

    if len(lst2) > min_length:
        merged_list.extend(lst2[min_length:])

    return merged_list


list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d"]

result = alternate_merge(list1, list2)
print(result)
