# Генерация последовательности
# 1. Функция generate_sequence(n, m): создает список из n элементов.
# 2. Генератор списка [i**2 + m for i in range(n)]
# 3. Вывод результата
#
# пример:
#
# вход:
# 5, 3
#
# выход:
# [3, 4, 7, 12, 19]

def generate_sequence(n, m):
    return [i**2 + m for i in range(n)]

n = 5
m = 3
result = generate_sequence(n, m)
print(result)
