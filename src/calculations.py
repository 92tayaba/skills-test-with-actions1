import math


def area_of_circle(radius):
    """Calculate the area of a circle with the given radius."""
    if radius < 0:
        return 0  # Avoid negative radii
    return math.pi * radius * radius


def get_nth_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        return 0  # Handle negative input
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
