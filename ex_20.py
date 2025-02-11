def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    if len(str1) != len(str2):
        raise ValueError("Списки должны иметь одинаковые буквы")
        return False
    char_list = list(str1)
    for i in str2:
        if i in char_list:
            char_list.remove(i)
        else:
            return False
    return len(char_list) == 0


print(is_anagram("Listen", "Silent"))
print(is_anagram("Hello", "World"))
print(is_anagram("Debit Card", "Bad Credit"))
print(is_anagram("Astronomer", "Moon starer"))
