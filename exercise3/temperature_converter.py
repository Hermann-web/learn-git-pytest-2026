# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_fahrenheit(c):
    return round(c * 9/5 + 32, 1)
def celsius_to_kelvin(c: Temperature) -> Temperature:
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    return round(k - 273.15, 2)