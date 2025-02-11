# Удаление дубликатов из списка
#
# Структура Задачи:
#
# 1. Получить список
# 2. Удалить все дубликаты
#
# пример:
#
# вход:
# [1, 2, 3, 1, 4, 2, 5]
#
# выход:
# [1, 2, 3, 4, 5]

def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

input_list = [1, 2, 3, 1, 4, 2, 5]
result = remove_duplicates(input_list)
print(result)
