def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    clean_s = "".join(s.split()).lower()
    return clean_s == clean_s[::-1]

def capitalize_words(s: str) -> str:
    return s.title()