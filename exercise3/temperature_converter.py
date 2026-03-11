from typing import Union

Temperature = Union[int, float]

def celsius_to_fahrenheit(celsius: Temperature) -> float:
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius: Temperature) -> float:
    return celsius + 273.15

def kelvin_to_celsius(kelvin: Temperature) -> float:
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    return kelvin - 273.15
