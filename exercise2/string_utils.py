# Exercise 2: String Utilities


def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in "aeiou")

def is_palindrome(s):
    clean_s = s.lower().replace(" ", "")
    return clean_s == clean_s[::-1]

def capitalize_words(s):
    return s.title()