# Class Object Attributes

class Person:
    # Class Object Attributes
    is_person = True

    # Constructor
    def __init__(self, name, lastname, age):
        # Attributes
        if age >= 18:
            self.name = name
            self.lastname = lastname
            self.age = age

    # Method
    def message(self):
        return f'My name is: {self.name} {self.lastname}, and my age is {self.age}.'


# Instance/Object of the Person class
person_obj1 = Person('Jason', 'Mamoa', 18)

person_obj2 = Person('James', 'Bond', 20)

# Access the methods
print(person_obj1.message())
print(person_obj2.message())
