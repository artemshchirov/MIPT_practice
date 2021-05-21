def fib(n):
    """
    Calculate Fibonacci number n.
    Raise TypeError if n != int
    Raise ValueError if n < 0 or n > 10000

    :param n: 0 < int < 99999
    :return: int > 0

    # doctests:
    >>> fib(1)
    1
    >>> fib(10)
    55
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work only with <class 'int'> type.")
    if n < 0:
        raise ValueError("Fibonacci can`t work with negative numbers.")
    if n >= 10000:
        raise ValueError("Fibonacci can`t work with numbers larger than 9999.")
    if n == 0:
        return 0
    f_1 = 1
    f_2 = 0
    for i in range(2, n + 1):
        f_1, f_2 = (f_1 + f_2), f_1
    return f_1


if __name__ == "__main__":
    import doctest
    doctest.testmod()
