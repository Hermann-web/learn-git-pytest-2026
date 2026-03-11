# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(c: Temperature) -> float:
    return round(c*9/5 + 32)
    


def fahrenheit_to_celsius(f) -> float:
    return round((f - 32) × 5/9)


def celsius_to_kelvin(C) -> float:
    return round(C + 273.15)
  


def kelvin_to_celsius(k) -> float:
    return round(k - 273.15)
  