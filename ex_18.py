# написать программу, которая объединяет и сортирует два списка
#
# пример:
#
# вход:
# [1, 3, 5], [2, 4, 6]
#
# выход:
# [1, 2, 3, 4, 5, 6]

def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    sorted_list = sorted(merged_list)
    return sorted_list

list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_and_sort_lists(list1, list2)
print(result)
