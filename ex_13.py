# Перестановка элементов двух списков
# 1. Функция swap_if_greater(lst1, lst2): меняет элементы местами
# 2. перебор элементов
# 3. Замена местами, если первое большое второго
#
# пример:
#
# вход:
# [5, 1, 9, 3] [2, 6, 8, 4]
#
# выход:
#
# ([2, 1, 8, 3] [5, 6, 9, 4])

def swap_if_greater(lst1, lst2):
    if len(lst1) != len(lst2):
        raise ValueError("Списки должны быть одинаковой длины")

    for i in range(len(lst1)):
        if lst1[i] > lst2[i]:
            lst1[i], lst2[i] = lst2[i], lst1[i]

    return lst1, lst2

lst1 = [5, 1, 9, 3]
lst2 = [2, 6, 8, 4]
result = swap_if_greater(lst1, lst2)
print(result)
