# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
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
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


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
    # Nettoyer la chaîne : enlever les espaces et mettre en minuscule
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    # Comparer avec son inverse
    return cleaned == cleaned[::-1]


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    if not s:
        return s  # Return the empty string if input is empty
    n = len(s)
    s0 = s[0].upper()
    for i in range(1, n):
        if s[i-1] == ' ':
            s0 += s[i].upper()
        else:
            s0 += s[i]
    return(s0)
