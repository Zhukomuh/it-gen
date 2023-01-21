def save_str_decorator(cls):
    """write result of cls.__str__ to {cls.__name__}.txt file"""

    def inner(*args, **kwargs):
        file_name = cls.__name__
        cls.__init__(cls, *args, **kwargs)
        with open(f'{file_name}.txt', 'w') as file:
            file.write(f'{cls.__str__(cls)}')

        return cls

    return inner


@save_str_decorator
class Dog:
    def __init__(self):
        self.color = 'Black'

    def __str__(self):
        return f'Woof-woof'


pug = Dog()
