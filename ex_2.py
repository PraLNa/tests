# lst = [1, 2, 3, 4, 5]
# shift = 2
#
# shift = shift % len(lst)
#
# shifted_list = lst[-shift:] + lst[:-shift]
#
# print(shifted_list)
#
#
# сдвиг списка
# напишите программу, которая сдвигает элементы списка на указанное количество позиций вправо.
# Если сдвиг больше длины списка, он должен повторяться
#
# пример:
# shift_list([1, 2, 3, 4, 5], 2)

def shift_list(lst, positions):
    if not lst:
        return lst
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]

result = shift_list([1, 2, 3, 4, 5], 2)
print(result)
