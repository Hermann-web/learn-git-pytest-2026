def celsius_to_fahrenheit(celsius: Temperature) -> float:
    # Formule : F = C × 9/5 + 32
    result = celsius * 9/5 + 32
    return round(result, 2)


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    # Formule : C = (F - 32) × 5/9
    result = (fahrenheit - 32) * 5/9
    return round(result, 2)


def celsius_to_kelvin(celsius: Temperature) -> float:
    # Formule : K = C + 273.15
    result = celsius + 273.15
    return round(result, 2)


def kelvin_to_celsius(kelvin: Temperature) -> float:
    # On vérifie d'abord le zéro absolu pour valider le test d'exception
    if kelvin < 0:
        raise ValueError("Temperature below absolute zero")
    
    # Formule : C = K - 273.15
    result = kelvin - 273.15
    return round(result, 2)