# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    fahrenheit = celsius * 9/5 + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)



def celsius_to_kelvin(celsius: Temperature) -> float:
    kelvin = celsius + 273.15
    return round(kelvin, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero (0 K)")
    
    celsius = kelvin - 273.15
    return round(celsius, 2)