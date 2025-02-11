# проверка на анаграмму
#
# Структура задачи:
#
# 1. Получить две строки
# 2. Проверть, являются ли они анаграммами (состоят из одинаковых букв, но в разном порядке)
#
# пример:
#
# вход:
# listen
# silent
#
# выход:
# True

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

input_str1 = "listen"
input_str2 = "silent"
output = are_anagrams(input_str1, input_str2)
print("Вход:", input_str1, "и", input_str2)
print("Выход:", output)