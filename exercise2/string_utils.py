def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    return sum(1 for char in s.lower() if char in "aeiou")

def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def capitalize_words(s: str) -> str:
    return s.title()