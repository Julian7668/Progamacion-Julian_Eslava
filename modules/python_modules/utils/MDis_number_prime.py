def is_number_prime(n: int) -> bool:
    """
    Verifica si un número entero es primo.

    Un número primo es aquel mayor que 1 que no tiene divisores positivos
    distintos de 1 y sí mismo.

    Args:
        n: Número entero a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.

    Examples:
        >>> is_number_prime(2)
        True
        >>> is_number_prime(4)
        False
        >>> is_number_prime(17)
        True
    """
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i: int = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    # Ejemplos de números primos
    test_numbers: tuple[int, ...] = (2, 3, 4, 5, 17, 18, 23, 24, 125)
    print("Verificación de números primos:")
    for num in test_numbers:
        print(f"{num}: {'Es primo' if is_number_prime(num) else 'No es primo'}")
