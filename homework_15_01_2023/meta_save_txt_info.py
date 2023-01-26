class Meta(type):
    """ This class intercepts information about the class being processed and
    write it to 'info.txt'."""
    def __new__(cls, name, base, attrs):
        return type.__new__(cls, name, base, attrs)

    def __init__(cls, name, base, attrs):
        super().__init__(name, base, attrs)
        with open('info.txt', 'a') as file:
            file.writelines(f'{name} : {[item for item in attrs]}\n')


class A(metaclass=Meta):
    def __init__(self):
        self.a = 123
        self.b = 'ser'

    def __str__(self):
        return f'test'


class B(metaclass=Meta):

    def __str__(self):
        return f'test1'


if __name__ == '__main__':
    a = A()
    b = B()