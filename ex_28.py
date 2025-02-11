# Сортировка слов в предложении по длине
#
# Структура задачи:
#
# 1. Получить строку
# 2. Отсортировать слова по длине
#
# пример:
#
# вход:
# Python is a very powerful language
#
# выход:
# ['is', 'a', 'very', 'Python', 'language', 'powerful']

def sort_words_by_length(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=len)
    return sorted_words

input_sentence = input("Введите предложение: ")
result = sort_words_by_length(input_sentence)
print(result)
