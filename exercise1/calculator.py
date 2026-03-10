# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of a and b.
    Returns:
        The sum of a and b
    """
    # TODO: Implement this function
    pass

    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Returns:
        The result of a - b
    """
    # TODO: Implement this function
    pass

    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Returns:
        The product of a and b
    """
    # TODO: Implement this function
    pass

    return a * b

def divide(a: Number, b: Number) -> Number:
    """
    Raises:
        ValueError: If b is 0
    """
    # TODO: Implement this function
    pass
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b