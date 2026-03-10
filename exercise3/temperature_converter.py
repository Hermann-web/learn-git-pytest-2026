# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]



Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius: float) -> float:
   
    f = celsius * 9/5 + 32
    return round(f, 2)

    Formula: F = C × 9/5 + 32

    Args:
        celsius: Temperature in Celsius
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    
    c = (fahrenheit - 32) * 5/9
    return round(c, 2)

    Returns:
        Temperature in Fahrenheit (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass

def celsius_to_kelvin(celsius: float) -> float:
    
    k = celsius + 273.15
    return round(k, 2)

def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9
def kelvin_to_celsius(kelvin: float) -> float:
    
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Kelvin (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convert temperature from Kelvin to Celsius.

    Formula: C = K - 273.15

    Args:
        kelvin: Temperature in Kelvin

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)

    Raises:
        ValueError: If kelvin is less than 0 (below absolute zero)
    """
    # TODO: Implement this function
    pass
    c = kelvin - 273.15
    return round(c, 2)