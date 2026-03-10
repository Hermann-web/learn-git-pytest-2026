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
    A=["a","e","i","o","u"]
    S=s.lower()
    j=0
    for i in S:
        if i in A :
            j+=1
    return j



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
    s_r= s.replace(" "," ").lower()
    return s_r ==reverse_string()
    


def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    if not s :
        return ""
    else:
        L=s.split()
        T=[]
        for i in L:
            a=i[0]
            b=i[1:]
            c=a.upper() + b 
            T.append(c)
    return " ".join(T)