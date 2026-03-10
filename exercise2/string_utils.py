# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    r=''
    for i in range(1,len(s)+1):
        r+=s[-i]
    return r
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
    vow=['a','e','i','o','u']
    s=s.lower()
    res=0
    for i in s:
        if i in vow: res+=1
    return res

    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    s=s.replace(" ","").lower()
    
    return s == reverse_string(s)
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
    pass


def capitalize_words(s: str) -> str:
    if s=='': return ''
    sl= [i for i in s]
    sl[0]= sl[0].upper()
    for j in range(len(sl)):
        if sl[j]==' ':
            if sl[j+1]!= ' ':
                sl[j+1]= sl[j+1].upper()
    res= ''
    for k in sl:
        res+=k
    return res
            

    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    pass
