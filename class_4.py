
class Person:

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class Student(Person):
    
    def __init__(self, name, number):
        super().__init__(name)
        self._number = number

    def set_number(self,number):
        self._number = number

    def get_number(self):
        return self._number

students = [
    ["Luis Cardenas", 123234235],
    ["Sarah Cardenas", 234234235],
    ["Cocoa beans", 235245345]
]

x = 0
for _ in range(3):
    person = students[x][0]
    id = students[x][1]

    student = Student(person, id)

    name = student.get_name()
    number = student.get_number()
    print(name, number)
    x += 1