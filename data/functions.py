from datetime import datetime


def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number.

    :param n: The index of the Fibonacci number to calculate. Must be a positive integer.
    :return: The nth Fibonacci number.
    :rtype: int
    """
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)


def get_fibonacci_from_current_day_number() -> int:
    """
    Calculates the Fibonacci number corresponding to the current day of the month plus one.

    :return: The Fibonacci number corresponding to the current day of the month.
    :rtype: int
    """
    return fib(datetime.now().day + 1)
            