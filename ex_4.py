list1 = [1, 2, 3]
list2 = [4, 5, 6]

if len(list1) != len(list2):
    raise ValueError("Списки должны быть одинаковой длины")

combined = [a + b for a, b in zip(list1, list2)]

print(combined)
