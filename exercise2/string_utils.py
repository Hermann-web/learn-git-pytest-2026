# Exercise 2: String Utilities
def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels="aeiou"
    count=0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count



def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ","").lower()
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    return s.title()