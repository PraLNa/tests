# Проверка на подстроку без in
#
# Структура задачи:
#
# 1. Получить две строки s1 и s2
# 2. Проверить, содержиться ли s2 в s1 без использования in
#
# пример:
#
# вход:
# hello world
# wor
#
# выход:
# True

def contains_substring(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s2 == 0:
        return True
    if len_s2 > len_s1:
        return False
    for i in range(len_s1 - len_s2 + 1):
        match = True
        for j in range(len_s2):
            if s1[i + j] != s2[j]:
                match = False
                break
        if match:
            return True

    return False

s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")

result = contains_substring(s1, s2)
print(result)
