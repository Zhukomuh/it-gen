import time


class Cat:
    def __init__(self, breed: str, color: str, name: str, age: int, file_name: str):
        self.breed = breed
        self.color = color
        self.name = name
        self.__age = age
        self.file_name = file_name

    age = property()

    @age.setter
    def age(self, age_val):
        with open(self.file_name, 'a') as file:
            seconds = time.time()
            file.writelines(f'{time.ctime(seconds)} :set age = {age_val} \n')
        self.__age = age_val



c1 = Cat('Royal', 'Grey', 'Starlight', 2, 'file.txt')
c1.age =3