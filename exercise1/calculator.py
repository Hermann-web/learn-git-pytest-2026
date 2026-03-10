# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Additionne deux nombres"""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Soustrait deux nombres"""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Multiplie deux nombres"""
    return a * b

def divide(a: Number, b: Number) -> float:
    """Divise deux nombres. Lève une erreur si division par zéro."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

