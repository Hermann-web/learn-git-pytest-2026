# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    
    c=a+b
    return c

    
   

def subtract(a: Number, b: Number) -> Number:
    return b-a
   
    


def multiply(a: Number, b: Number) -> Number:
    
    
   
    return a*b


def divide(a: Number, b: Number) -> Number:
    if b==0 :
        return None
    else :return a/b
