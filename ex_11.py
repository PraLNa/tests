# Сдвиг списка влево
# 1. Функция shift_left(lst, k): принимает список и число k, сдвигает влево
# 2. Обрезка списка и перестановка частей местами
# 3. Возврат нового списка
#
# пример:
#
# вход:
#
# [1, 2, 3, 4, 5], 2
#
# выход:
#
# [3, 4, 5, 1, 2]

def shift_left(lst, k):
    if not lst or k == 0:
        return lst

    n = len(lst)

    k = k % n

    return lst[k:] + lst[:k]


input_list = [1, 2, 3, 4, 5]
shift_amount = 2
result = shift_left(input_list, shift_amount)
print(result)
