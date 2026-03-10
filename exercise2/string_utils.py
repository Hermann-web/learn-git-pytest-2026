# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    chaine= s 
    inverse=chaine[::-1]
    return inverse

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in s:
        if char in vowels:
            count += 1
            
    # TRÈS IMPORTANT : Le return doit être aligné avec le 'for'
    # S'il est décalé à droite, il s'arrête trop tôt !
    return count
def is_palindrome(s: str) -> bool:
    # We clean the string (lowercase and remove spaces) to make it accurate
    clean_s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return clean_s == clean_s[::-1]


def capitalize_words(s: str) -> str:
    return s.title()
