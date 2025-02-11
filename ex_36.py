# Перемешивание элементов списка
#
# структура задачи:
#
# 1. Получить список
# 2. Перемешать его элементы случайным образом
#
# пример:
#
# вход:
# [1, 2, 3, 4, 5]
#
# выход:
# [3, 1, 5, 2, 4]

import random

def shuffle_list(input_list):
    # Перемешиваем элементы списка
    random.shuffle(input_list)
    return input_list

# Получаем список от пользователя
input_string = input("Введите элементы списка через запятую: ")
input_list = [int(x) for x in input_string.split(",")]

# Вызываем функцию и получаем результат
shuffled_list = shuffle_list(input_list)

# Выводим результат
print(f"Перемешанный список: {shuffled_list}")
