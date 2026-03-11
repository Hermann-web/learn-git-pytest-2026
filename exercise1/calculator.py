# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    resultat= a+b
    print("Le résultat est ", resultat)
    return resultat


def subtract(a: Number, b: Number) -> Number:
   resultat= a-b
   print("Le résultat est", resultat)
   return resultat



def multiply(a: Number, b: Number) -> Number:
    resultat=a*b
    print("Le résultat est", resultat)
    return resultat



def divide(a: Number, b: Number) -> Number:
    if b==0:
        raise ValueError("Cannot divide by zero")
    else:
        print("Le résultat est",resultat)
    return resultat

