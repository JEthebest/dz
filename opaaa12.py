# class Car:
#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color

# tayota = Car('tayota', 'avalon', 'white')

# print(f'{tayota.brand}  {tayota.model}  {tayota.color}')


# class Employee:
#     def __init__(self, name, gender, surname, birth):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.birth = birth

#     def __str__(self):
#         return f'{self.name}, {elf.surname}, {self.gender}, {self.birth}'

# templ = Employee('egor', 'man', 'averin', '02.12.2010')


class Human:
    def __init__(self, name, age, fav_less):
        self.name = name
        self.age = age
        self.fav_less = fav_less

    def __str__(self):
        return f'{self.name}, {self.age}, {self.fav_less}'

class Teacher(Human):
    def __init__(self, speciality, salary):
        self.speciality = speciality
        self.salary = salary

    def __str__(self):
        return f'{self.speciality}, {self.salary}'
    
class Student(Human):
    def __init__(self, grade):
        self.grade = grade

    def __str__(self):
        return f'{self.grade}, {self.favour_les}'

bel = Human('alla', '43', 'chemistri')
bel1 = Teacher('himichka', '12000')
bel2 = Student('4')
print(bel)
print(bel1)
print(bel2)








