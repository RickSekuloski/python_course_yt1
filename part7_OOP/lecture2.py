# Class Constructor, Attributes and Methods

class Person:
    # Constructor
    def __init__(self, name, lastname, age):
        # Attributes
        self.name = name
        self.lastname = lastname
        self.age = age

    # Method
    def message(self):
        print(f'My name is: {self.name} {self.lastname}, and my age is {self.age}')


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
person_obj1.message()
# Access the methods
person_obj2.message()
