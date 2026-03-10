# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.
    Returns:
        The reversed string
    """
    # TODO: Implement this function
    pass

    return s[::-1]

def count_vowels(s: str) -> int:
    """
    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    pass

    vowels = set('aeiouAEIOU')
    return sum(1 for char in s if char in vowels)

def is_palindrome(s: str) -> bool:
    """
    Returns:
        True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    pass

    cleaned = ''.join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]

def capitalize_words(s: str) -> str:
    """
    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    pass
    return ' '.join(word.capitalize() for word in s.split())