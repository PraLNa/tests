numbers = [10, 3, 5, 20, 1]

if not numbers or len(numbers) < 2:
    raise ValueError("Список должен содержать как минимум два элемента.")

min_num = min(numbers)
max_num = max(numbers)

max_difference = max_num - min_num

print(max_difference) 
