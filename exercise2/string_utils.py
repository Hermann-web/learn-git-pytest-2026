# Exercise 2: String Utilities

def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def is_palindrome(s: str) -> bool:
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

def capitalize_words(text: str) -> str:
    # On sépare par un espace strict, on met en majuscule, puis on recolle
    return " ".join([word.capitalize() for word in text.split(" ")])
 