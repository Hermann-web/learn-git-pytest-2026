# Exercise 2: String Utilities



def reverse_string(s: str) -> str:
    """Inverse une chaîne de caractères"""
    return s[::-1]

def count_vowels(s: str) -> int:
    """Compte le nombre de voyelles dans une chaîne"""
    return sum(1 for c in s if c.lower() in "aeiou")

def is_palindrome(s: str) -> bool:
    """Vérifie si une chaîne est un palindrome"""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def capitalize_words(s: str) -> str:
    """Met la première lettre de chaque mot en majuscule"""
    return s.title()