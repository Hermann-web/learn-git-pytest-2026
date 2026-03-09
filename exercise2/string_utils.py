# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    v = "aeiouAEIOU"
    j=0
    for i in s:
        if i in v:
            j+=1
    return j


def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
   return s.title()
