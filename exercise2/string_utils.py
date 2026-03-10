# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # Implémentation de la fonction
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # Définition des voyelles
    vowels = "aeiouAEIOU"
    # Comptage des voyelles dans la chaîne
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Nettoyage de la chaîne : suppression des espaces et passage en minuscules
    cleaned = s.replace(" ", "").lower()
    # Vérification du palindrome
    return cleaned == cleaned[::-1]


def capitalize_words(text):
    result = ""
    capitalize_next = True
    for char in text:
        if char.isspace():
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char.lower()
    return result