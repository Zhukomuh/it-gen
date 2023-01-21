def save_str_decorator(cls):
    """write result of cls.__str__ to {cls.__name__}.txt file"""
    file_name = cls.__name__
    with open(f'{file_name}.txt', 'w') as file:
        file.write(f'{cls.__str__(cls)}')

    return cls


@save_str_decorator
class Dog:
    def __str__(self):
        return f'Woof-woof'


