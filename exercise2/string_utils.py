# Exercise 2: String Utilities


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def capitalize_words(s):
    return s.title()