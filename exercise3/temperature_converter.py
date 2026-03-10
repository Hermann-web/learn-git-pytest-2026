# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    temp = celsius*(9/5)+ 32
    return round(temp, 2)



def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    return (fahrenheit - 32) * (5/9)


def celsius_to_kelvin(celsius: Temperature) -> float:
    return   celsius + 273.15



def kelvin_to_celsius(kelvin: Temperature) -> float:
    if kelvin < 0 :
        raise ValueError("Temperature cannot be below absolute zero")
    else :
        temp = kelvin - 273.15
    return round (temp, 2)

