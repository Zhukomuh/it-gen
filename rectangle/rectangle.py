"""class for create rectangle and work with param data"""


class Rectangle:
    """create rectangle obj with length and height param"""

    def __init__(self, length: int | float, height: int | float):
        if length == 0:
            raise ZeroDivisionError("length can't be equal 0")
        if height == 0:
            raise ZeroDivisionError("height can't be equal 0")
        self.length = length
        self.height = height

    def area(self):
        return self.height * self.length

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __mul__(self, other: int | float):
        return self.area() * other

    def __add__(self, other):
        return self.area() + other.area()

    def __str__(self):
        return f'Rectangle with length: {self.length} and height: {self.height}\nArea: {self.area()}'


if __name__ == '__main__':
    ab = Rectangle(10, 5)
    bc = Rectangle(5, 6)
    print(ab)
    print(bc)
    print(ab > bc)
    print(ab < bc)
    print(ab + bc)
    print(ab * 5)
