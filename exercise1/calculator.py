from numbers import Number


def add(a: Number, b: Number) -> Number:
    """
    Return the sum of a and b.
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Return the result of subtracting b from a.
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of a and b.
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Return the result of dividing a by b.

    Raises:
        ZeroDivisionError: If b is 0
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
