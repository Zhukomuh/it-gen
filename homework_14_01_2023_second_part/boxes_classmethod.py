class Box:
    """Class Box with staticmethod which
    sum volume of two Box object"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.volume = self.x * self.y * self.z

    @staticmethod
    def sum(box1, box2):
        return f'{box1.volume} + {box2.volume} = {box1.volume + box2.volume}'



