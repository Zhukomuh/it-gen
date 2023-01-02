from student_group import student,group

if __name__ == '__main__':
    bob = student.Student('Bob', 'Dylan', 56)
    alex = student.Student('Alex', 'Novos', 33)
    chris = student.Student('Chris', 'Miller', 22)
    it_gen = group.Group('python it gen')
    it_gen.add_student(bob)
    it_gen.add_student(alex)
    it_gen.add_student(chris)
    print(it_gen)
    it_gen.del_student(chris)
    print(it_gen)