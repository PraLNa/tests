# поиск самого длинного слова в списке
# 1. Функция longest_word(words): принимает список строк и находит самую длинную строку
# 2. Перебор списка и нахождение максимального по длине слова
# 3. Возврат результата
#
# пример:
#
# вход:
# ["яблоко", "банан", "ананас", "черешня"]
#
# выход:
#
# черешня

def longest_word(words):
    if not words:
        return None

    max_word = ""

    for word in words:
        if len(word) > len(max_word):
            max_word = word

    return max_word

words_list = ["яблоко", "банан", "ананас", "черешня"]
result = longest_word(words_list)
print(result)
