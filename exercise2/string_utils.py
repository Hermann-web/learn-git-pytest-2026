# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    v = "aeiouAEIOU"
    j=0
    for i in s:
        if i in v:
            j+=1
    return j


def is_palindrome(s: str) -> bool:
    #We put everything in lowercase and remove the spaces to make comparison easier.
    b = s.lower().replace(" ", "")
    return b == b[::-1]


def capitalize_words(s: str) -> str:
   #title can capitalize the first letter of each word in the input string
   return s.title()  
