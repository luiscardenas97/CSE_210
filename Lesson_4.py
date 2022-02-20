# a regular class called Person
import numbers


class Person:                    

    def get_name(self):
        names = ["Joseph", "Luis", "Juan"]
        return names

# a class that inherits from Person
class Student(Person):

    def get_number(self):
        numbers = ["0123456789", "12433413123","23857234834"]
        return numbers

class Age(Student):

    def get_age(self):
        ages = ["23","50","42"]
        return ages


# the student instance automatically has the get_name() method!
ages = Age()
x = 0
for _ in range(3):
    name = ages.get_name()[x]
    number = ages.get_number()[x]
    age = ages.get_age()[x]
    x += 1
    print(name, number, age)

# a parent class called Person
class Persona:                    

    def __init__(self, number):
        self._number = number

    def get_number(self):
        return self._number

# a child class called Student
class Estudiante(Persona):
    
    # invoking the parent constructor using "super"!
    def __init__(self, number):
        super().__init__(number)

estudiante = Estudiante("0123456789")
numero = estudiante.get_number()
print(numero)