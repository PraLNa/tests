# Подсчет количества слов в строке
#
# Структура задачи:
#
# 1. Получить строку
# 2. Подсчитать, сколько раз встречается каждое слово
#
# пример:
#
# вход:
# apple banana apple orange banana apple
#
# выход:
# ['apple', 3, 'banana', 2, 'orange', 1]

def count_words(input_string):
    words = input_string.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    result = []
    for word, count in word_count.items():
        result.append(word)
        result.append(count)

    return result

input_string = "apple banana apple orange banana apple"
output = count_words(input_string)
print(output)
