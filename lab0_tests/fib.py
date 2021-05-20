def fib(n):
    """
    Calculates fibonacci numbers

    >>> fib(1)
    1
    >>> fib(10)
    55
    >>> fib(-1)
    None
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
