class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0,next_value = 1):
        self.value = value
        self.next_value = next_value

    def next(self):
        F = Fib()
        F.value = self.next_value
        F.next_value = self.value + self.next_value
        return F

    def __repr__(self):
        return str(self.value)


