def is_number_prime(n: int) -> bool:
    return not n <= 1 and all(n % i for i in range(2, int(n**0.5) + 1))
