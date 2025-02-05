# numbers = [10, 3, 5, 20, 1]
#
# if not numbers or len(numbers) < 2:
#     raise ValueError("Список должен содержать как минимум два элемента.")
#
# min_num = min(numbers)
# max_num = max(numbers)
#
# max_difference = max_num - min_num
#
# print(max_difference)


# Максимальная разница
# напишите программу, которая принимает список чисели возвращает
# максимальную разницу между двумя любыми элементами списка
#
# пример:
# max_difference([10, 3, 5, 20, 1])

def max_difference(numbers):
    if len(numbers) < 2:
        raise ValueError("Список должен содержать как минимум два элемента.")

    max_num = max(numbers)
    min_num = min(numbers)

    return max_num - min_num

result = max_difference([10, 3, 5, 20, 1])
print(result)
