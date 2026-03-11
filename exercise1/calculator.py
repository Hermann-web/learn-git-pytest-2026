# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a,b):
    return a+b
   


def subtract(a,b):
    return a-b


   


def multiply(a,b):
    return a*b
    


def divide(a,b):
    if b==0 raise ValueError 
    else:
        return a/b




