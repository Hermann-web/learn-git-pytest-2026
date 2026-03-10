# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]
  


def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0 
    for j in s :
        if j in vowels :
            count=count +1 
    return count

def is_palindrome(s: str) -> bool:
    a = "".join(s.split()).lower()
    return a==a[::-1]






def capitalize_words(s: str) -> str:
    newstr = s.title()
    return newstr







    



