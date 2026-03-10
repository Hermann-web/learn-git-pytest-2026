# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32
    """
    # Calculate Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    
    # Return rounded to 2 decimal places as requested
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9
    """
    # Parentheses ensure the subtraction happens first
    celsius = (fahrenheit - 32) * 5/9
    
    # Round to 2 decimal places
    return round(celsius, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15
    """
    kelvin = celsius + 273.15
    
    # Return rounded to 2 decimal places as per requirements
    return round(kelvin, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convert temperature from Kelvin to Celsius.

    Formula: C = K - 273.15
    """
    # Check for temperatures below absolute zero
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero.")
    
    celsius = kelvin - 273.15
    
    return round(celsius, 2)