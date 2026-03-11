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
    return(s[::-1])



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
    so=0
    l="aeiouAEIOU"
    for x in s:
        if x in l:
            so+=1
    return so


def is_palindrome(s: str) -> bool:
    s = s.replace(" ","").lower()
    return s == s[::-1]
   


def capitalize_words(s:str) -> str:
    return s.title()
    