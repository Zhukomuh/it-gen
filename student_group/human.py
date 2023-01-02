"""base class for create human"""


class Human:
    """create 'human' object with name, lastname, age param"""

    def __init__(self, name: str, lastname: str, age: int):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self):
        """reformat __str__ method for better output inform about object"""
        return f'{self.name} {self.lastname}, {self.age} years old'
