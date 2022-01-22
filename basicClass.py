'Part.1'

#Attributes and behaviors
#Idea of a person (class). A real physical thing (objects).
#Class theory of something
#Another way of thinking compare to functions. Using objects.
class Person:
    pass

#Instantiate the class
#Object is an object
adam = Person()
print(adam)

#dot notation attribute for a person.
adam.full_name = "Adam Hayes"
print(adam.full_name)


'Part.2'

class Person:
    #Functions in a class are called methods.
    #___ Private 
    #___int___ constructor. What builds or instantiates a method.
    #To create an instant of something - Instantiates.
    # Every method starts with a argument called self. Just the first method has argument self.
    def __init__(self):
        pass

#Instant of the class. Instantiate. 
adam = Person()
print(adam)

heather = Person()
print(heather)


'Part.3'

class Person:
    #Pass things in my method.
    #Pass a parameter
    def __init__(self, full_name=""): #TO MAKE IT OPTIONAL 
        #It takes what you pass and store it in itself.
        self.full_name = full_name

    #def _str_(self):
    #     return f"{self.full_name} is a {self.__class__}"
    
#adam is an instance of a class.
#float, lists are classes
adam = Person("Adam Hayes")
print(adam)
print(adam.full_name)
heather = Person("Heather Purser")
print(heather)
print(heather.full_name)

aubury = Person("Aubury Orr")
print(aubury.full_name)



class Restaurant:
    #__init__ 
    def __init__(self, name, cuisine, price, rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return 

#Instantiate something
adam = Person("Adam Hayes")
print(adam)
print(adam.full_name)


