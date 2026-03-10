# Exercise 3: Temperature Converter

from typing import Union

def celsius_to_fahrenheit(c: Union[int, float]) -> Union[int, float]:
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    return k - 273.15
