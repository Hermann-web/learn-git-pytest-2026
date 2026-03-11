def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.upper() if c in "AEIOU")

def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def capitalize_words(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == " ":
            result.append(" ")
            i += 1
        else:
            j = i
            while j < len(s) and s[j] != " ":
                j += 1
            word = s[i:j]
            result.append(word[0].upper() + word[1:])
            i = j
    return "".join(result)
