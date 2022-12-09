class Human:
    def __init__(self, name: str, lastname: str, age: int):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return f'{self.name} {self.lastname}, {self.age} years old'


class Student(Human):
    def __str__(self):
        return f'{self.lastname} {self.name[0]}.'


class Group:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.group_members = []

    def add_student(self, student):
        if len(self.group_members) <= 10:
            if student not in self.group_members:
                self.group_members.append(student)
            else:
                raise Exception('Student is already in a group')
        else:
            raise Exception('Group is already full')

    def del_student(self, student):
        if student in self.group_members:
            self.group_members.remove(student)
        else:
            raise Exception('Student is not in a group')

    def __str__(self):
        return f'{self.group_name}: ' + ','.join(map(str, self.group_members))


if __name__ == '__main__':
    bob = Student('Bob', 'Dylan', 56)
    alex = Student('Alex', 'Novos', 33)
    chris = Student('Chris', 'Miller', 22)
    it_gen = Group('python it gen')
    it_gen.add_student(bob)
    it_gen.add_student(alex)
    it_gen.add_student(chris)
    print(it_gen)
    it_gen.del_student(chris)
    print(it_gen)