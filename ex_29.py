# Удаление всех гласных из строки
#
# Структура Задачи:
#
# 1. Получить строку
# 2. Удалить все гласные(aeiouAEIOU)
#
# пример:
#
# вход:
# Hello World
#
# выход:
# Hll wrld

def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in sentence if char not in vowels)
    return result

input_sentence = input("Введите строку: ")
result = remove_vowels(input_sentence)
print(result)
