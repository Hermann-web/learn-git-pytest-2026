from typing import Union

Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    result = (celsius * 9 / 5) + 32
    return round(result, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """Convert temperature from Fahrenheit to Celsius."""
    result = (fahrenheit - 32) * 5 / 9
    return round(result, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    """Convert temperature from Celsius to Kelvin."""
    result = celsius + 273.15
    return round(result, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """Convert temperature from Kelvin to Celsius."""
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    result = kelvin - 273.15
    return round(result, 2)