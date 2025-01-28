strings = ["level", "hello", "world", "radar"]

def is_palindrome(s):
    return s == s[::-1]

palindromes = list(filter(is_palindrome, strings))

print(palindromes)