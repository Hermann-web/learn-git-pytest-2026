# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return round((celsius * 9/5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return round((fahrenheit - 32) * 5/9, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Kelvin.
    """
    return round(celsius + 273.15, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convert temperature from Kelvin to Celsius.
    """
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero")
    return round(kelvin - 273.15, 2)