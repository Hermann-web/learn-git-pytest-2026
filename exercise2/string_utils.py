# Exercise 2: String Utilities
def reverse_string(s: str) -> str:
    # L'astuce magique de Python pour inverser du texte !
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiou"
    count = 0
    # s.lower() permet de tout transformer en minuscules pour ne rien rater
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def is_palindrome(s: str) -> bool:
    # 1. On met tout en minuscules (.lower())
    # 2. On remplace les espaces par "rien" pour les effacer (.replace(" ", ""))
    cleaned_s = s.lower().replace(" ", "")
    
    # On vérifie si le mot nettoyé est égal à son inverse
    return cleaned_s == cleaned_s[::-1]

def capitalize_words(s: str) -> str:
    # Python a une fonction toute prête pour mettre des majuscules à chaque mot
    return s.title()