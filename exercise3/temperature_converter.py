# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    b = celsius * 9/5 + 32
    return round(b, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    d = (fahrenheit - 32) * 5/9
    return round(d, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    k = celsius + 273.15
    return round(k, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    
    c = kelvin - 273.15
    return round(c, 2)
