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


def get_transaction_info(transaction_func):
    """
    A decorator that wraps a transaction function (deposit or withdrawl) to return a list of strings
    representing the transaction information. The returned list contains the current time, the amount
    of the transaction, and the type of transaction (Credit or Debit).

    :param transaction_func: The transaction function to decorate.
    :return: A list of strings representing the transaction information.
    """
    def inner(*args):
        transaction_func(*args)
        time = datetime.now().strftime("%d %b %Y %H:%M:%S")
        amount = str(args[1])
        transaction = 'Credit' if transaction_func.__name__ == 'deposit' else 'Debit'
        return [time, amount, transaction]
    return inner

