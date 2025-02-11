# Поиск самого частого встречающегося элемента
#
# структура задачи:
#
# 1. Получить список
# 2. Найти самый часто встречающийся элемент
#
# пример:
#
# вход:
# [1, 2, 3, 1, 4, 1, 2]
#
# выход:
# 1

from collections import Counter

def most_frequent_element(input_list):
    count = Counter(input_list)
    most_common_element, _ = count.most_common(1)[0]
    return most_common_element

input_string = input("Введите элементы списка через запятую: ")
input_list = [int(x) for x in input_string.split(",")]
result = most_frequent_element(input_list)

print(f"Самый часто встречающийся элемент: {result}")
