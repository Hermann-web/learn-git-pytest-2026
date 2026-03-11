# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    X = "aeiouAEIOU"
    c = 0
    for y in s:
        if y in X:
            c += 1
    return c


def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def capitalize_words(s: str) -> str:
    return s.title()
#fin 