# Exercise 2: String Utilities

def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the string (case-insensitive).
    """
    return sum(1 for c in s.lower() if c in "aeiou")


def is_palindrome(s: str) -> bool:
    """
    Check if the string is a palindrome.
    Ignore spaces and case.
    """
    s_clean = ''.join(c.lower() for c in s if c.isalnum())  # remove spaces/punctuation
    return s_clean == s_clean[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the string.
    """
    return ' '.join(word.capitalize() for word in s.split(' '))