# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    reverse_string = ""
    for c in range(len(s)-1, -1, -1):
        reverse_string += s[c]
    return reverse_string


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    count_vowels = 0
    for c in s:
        if c in "aeiouAEIOU":
            count_vowels += 1
    return count_vowels


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
    cleaned_string = s.replace(" ", "").lower()
    return cleaned_string == reverse_string(cleaned_string)
    


# def capitalize_words(s: str) -> str:
#     """
#     Capitalize the first letter of each word in the input string.

#     Args:
#         s: Input string

#     Returns:
#         The input string with the first letter of each word capitalized
#     """
#     split_string = s.split() # Séparer la phrase en mots
#     capitalized_string = ""
#     for word in split_string:
#         capitalized_string += word.capitalize() + " " # Capitaliser chaque mot et ajouter un espace
#     return capitalized_string.strip() # Supprimer l'espace final à la fin de chaque mot capitalisé


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string 

    Returns:
        The input string with the first letter of each word capitalized
    """
    return s.title()