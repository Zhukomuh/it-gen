class_ref = []


def deco_reference(cls):
    """Adds references to the class that was called
    by this decorator in list(class_ref)"""
    class_ref.append(cls)
    return cls


class Decorator:
    """Adds references to the class that was called
        by this decorator in list(class_ref)"""
    class_ref = []

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        self.class_ref.append(self.cls)
        return self.cls


@Decorator
@deco_reference
class A:
    def __init__(self):
        self.a = 1
        self.b = 2


@Decorator
@deco_reference
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}'


if __name__ == '__main__':
    a = A()
    b = B(10, 14)
    print(class_ref)
    print(Decorator.class_ref)
