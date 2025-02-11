# Подсчет количества заглавных букв в строке
#
# пример:
#
# вход:
# Hello World
#
# выход:
# 2

def count_uppercase_letters(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            count += 1
    return count

input_string = "Hello World"
result = count_uppercase_letters(input_string)

print(result)
