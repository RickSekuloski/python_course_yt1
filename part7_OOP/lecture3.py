# Class Object Attributes

class Person:
    # Class Object Attributes
    is_person = True
    # Constructor
    def __init__(self, name, lastname, age):
        # Attributes
        self.name = name
        self.lastname = lastname
        self.age = age

    # Method
    def message(self):
        return f'My name is: {self.name} {self.lastname}, and my age is {self.age}.' \
               f' The value of the person_is attribute is: {Person.is_person}.' \
               f' The value of the person_is attribute is: {self.is_person}.'


# Instance/Object of the Person class
person_obj1 = Person('Jason', 'Mamoa', 40)
# Access the attributes
print(person_obj1.name)
print(person_obj1.lastname)
# print(person_obj1)

# Instance/Object of the Person class
person_obj2 = Person('James', 'Bond', 50)
# Access the attributes
print(person_obj2.name)
print(person_obj2.lastname)

# Access the methods
print(person_obj1.message())
# Access the methods
print(person_obj2.message())
