# Разворот каждого слова в строке
# Структура задачи:
# 1. Получить строку
# 2. Развернуть каждое слово отдельно, сохраняя порядок слов
#
# пример:
#
# вход:
# Hello world!
#
# выход:
# olleH !dlrow


def reverse_each_word(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    result = ' '.join(reversed_words)

    return result

input_string = "Hello World!"
output_string = reverse_each_word(input_string)
print("Вход:", input_string)
print("Выход:", output_string)