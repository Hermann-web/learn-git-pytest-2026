# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    n = len(s)
    return s[n - 1 : : -1]


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    voy = ['a', 'e', 'i', 'o', 'u',]
    nb_voy = 0
    for l in s:
        if l.lower() in voy:
            nb_voy += 1
    return nb_voy


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
    # TODO: Implement this function
    s_clean = s.lower().replace(" ", "")
    return s_clean == reverse_string(s_clean)


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    if not s:  # Cas de la chaîne vide
        return ""
    n = len(s)
    s0 = s[0].upper()
    for i in range(1, n):
        if s[i-1] == ' ':
            s0 += s[i].upper()
        else:
            s0 += s[i]
    return(s0)