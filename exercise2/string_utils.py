# Exercise 2: String Utilities

def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

def is_palindrome(s: str) -> bool:
    c = s.replace(" ", "").lower()
    m = 0
    for i in range(0, len(c)):
        j = i + 1
        if c[i] == c[-j]:
            m += 1
            
    if m == len(c):
        return True
    else:
        return False
        

def capitalize_words(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split(' '))