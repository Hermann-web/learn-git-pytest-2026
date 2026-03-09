# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    return celsius × 9/5 + 32
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    return (fahrenheit - 32) × 5/9
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)
    """
    # TODO: Implement this function
  


def celsius_to_kelvin(celsius: Temperature) -> float:
    return celsiu + 273.15
    """
    Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Kelvin (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    


def kelvin_to_celsius(kelvin: Temperature) -> float: 
    return kelvin - 273.15
    raise ValueError("kelvin<0")
    
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
    
