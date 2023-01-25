class StrDecorator:
    """add to result of cls.__str__ param text:str"""

    def __init__(self, text: str):
        self.text = text

    def __call__(self, cls):
        def inner(*args, **kwargs):
            cls.__init__(cls, *args, **kwargs)
            if cls.__str__:
                return f'{self.text} {cls.__str__(cls)}'
            return cls(*args, **kwargs)

        return inner


@StrDecorator(text='text1')
class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def __str__(self):
        return f'{self.a} ^ {self.b}'


@StrDecorator(text='text2')
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}'


a = A()
b = B(1, 3)
print(a)
print(b)
