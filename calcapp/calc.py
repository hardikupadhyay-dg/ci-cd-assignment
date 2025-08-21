def _validate(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")

def add(a: int, b: int) -> int:
    _validate(a, b)
    return a + b

def subtract(a: int, b: int) -> int:
    _validate(a, b)
    # define as non-negative result for positive integers
    if a < b:
        raise ValueError("For this demo, a must be >= b")
    return a - b

def product(a: int, b: int) -> int:
    _validate(a, b)
    return a * b
