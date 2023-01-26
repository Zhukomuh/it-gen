class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.__volume = x * y * z

    def __setattr__(self, key, value):
        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise ValueError('Attribute must be integer')

