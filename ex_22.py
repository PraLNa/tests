# поиск второго наибольшего числа в списке
#
# Структура задачи:
#
# 1. Получить список
# 2. Найти второе по величине число
#
# пример:
#
# вход:
# [10, 20, 4, 45, 99]
#
# выход:
# 45

def second_largest_number(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) < 2:
        return None

    return unique_numbers[1]

input_list = [10, 20, 4, 45, 99]
output = second_largest_number(input_list)
print("Вход:", input_list)
print("Второе по величине число:", output)