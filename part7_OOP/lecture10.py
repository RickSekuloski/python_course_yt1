# Private vs Public Variables

class Person:
    # Class Object Attributes
    is_person = True

    # Constructor with default values
    def __init__(self, name='John', lastname='Doe', age=19):
        # Attributes

        if age >= 18:
            self._name = name
            self._lastname = lastname
            self._age = age

    # Method
    def message(self):
        return f'My name is: {self._name} {self._lastname}, and my age is {self._age}.'


# Instance/Object of the Person class
person_obj1 = Person('Jason', 'Mamoa', 18)

# Access the methods
print(person_obj1.message())
print('*******************************************')

# Access the attributes
person_obj1._lastname = 'Bourne'
print(person_obj1.message())


