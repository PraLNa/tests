lst = [1, 2, 3, 4, 5]
shift = 2

shift = shift % len(lst)

shifted_list = lst[-shift:] + lst[:-shift]

print(shifted_list)
