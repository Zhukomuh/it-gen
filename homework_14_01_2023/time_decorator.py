import time
from functools import wraps


class TimeDecorator:
    """decorator class which counts the execution time of the function and write this information in file.
    With param quantity of iteration and file name"""

    def __init__(self, quantity: int, file: str):
        self.quantity = quantity
        self.file = file
        self.start = 0
        self.end = 0

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            self.start = time.time()
            for _ in range(1, self.quantity):
                func(*args, **kwargs)
            self.end = time.time()
            print(self.end - self.start, ' sec')
            with open(self.file, 'a') as file:
                file.writelines(f'Function: {func.__name__}. Quantity of iteration: {self.quantity}. '
                                f'Timing: {self.end - self.start} sec\n')
            return func(*args, **kwargs)

        return inner


@TimeDecorator(10000, 'test.txt')
def add(x, y):
    return x + y

@TimeDecorator(10000, 'test2.txt')
def mul(x, y):
    return x * y


if __name__ == '__main__':
    add(12, 4)
    mul(12,4)
