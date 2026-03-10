# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    Returns:
        Temperature in Fahrenheit (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass

    return round(celsius * 9/5 + 32, 2)

def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Returns:
        Temperature in Celsius (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass

    return round((fahrenheit - 32) * 5/9, 2)

def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Returns:
        Temperature in Kelvin (rounded to 2 decimal places)
    """
    # TODO: Implement this function
    pass

    return round(celsius + 273.15, 2)

def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Raises:
        ValueError: If kelvin is less than 0 (below absolute zero)
    """
    # TODO: Implement this function
    pass
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero")
    return round(kelvin - 273.15, 2)