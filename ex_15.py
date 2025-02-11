# перевод числа в двоичную систему
# 1. функция to_binary(n): переводит число в двоичную систему рекурсией.
# 2. Разбиение числа и возврат строкой
#
# пример:
#
# вход:
# 10
#
# выход:
# 1010

def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n // 2) + str(n % 2)

n = int(input())
print(to_binary(n))