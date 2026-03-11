# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return (s[::-1])


def count_vowels(s: str) -> int:
    e=0
    for i in s:
        if i in [a, e, o, i, u]:
            e+=1
    return e

def is_palindrome(s: str) -> bool:
    if reverse_string(s)==s:
        return True
    return False


def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]
    
    