# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    A=""
    n=len(s)
    for i in range(n):
        A=s[n-i]
    return A    

        
        


def count_vowels(s: str) -> int:
    A='aeiouyAEIOUY'
    B=s
    n=len(s)
    c=0
    for i in range(n):
        for j in range(len(A)):
            if s[i]==s[j]:
               c+=1
    return c           
        


def is_palindrome(s: str) -> bool:
    n=len(s)
    if s[0]==s[n]:
        return True
    else: return False     
        


def capitalize_words(s: str) -> str:
    A=''
    c=True # detecte le debut d un mot 
    for i in s :
      code-ascii=ord(i)
      if c==True and 97<=code-ascii<=112:
        A+=chr(code-ascii-32)
        c=False 
      else :
        A+=i 
        if i=='' :
            c=True
        else :
            c= False 
    return A   


       
    
    

