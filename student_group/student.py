"""create student obj from parents class 'Human'"""
from student_group import human


class Student(human.Human):
    def __str__(self):
        """reformat parent __str__ method"""
        return f'{self.lastname} {self.name[0]}.'
