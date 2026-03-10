from typing import Union

Temperature = Union[int, float]

def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """Convert Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """Convert Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

def celsius_to_kelvin(celsius: Temperature) -> float:
    """Convert Celsius to Kelvin."""
    return round(celsius + 273.15, 2)

def kelvin_to_celsius(kelvin: Temperature) -> float:
    """Convert Kelvin to Celsius. Raises ValueError if kelvin < 0."""
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    return round(kelvin - 273.15, 2)
