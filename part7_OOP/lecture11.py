# OOP - Inheritance & Method Overriding
# Person Class
class Person:
    # Class Object Attributes
    is_person = True

    # Constructor with default values
    def __init__(self, name='John', lastname='Doe', age=19):
        # Attributes

        if age >= 18:
            self.name = name
            self.lastname = lastname
            self.age = age

    # Method
    def message(self):
        return f'My name is: {self.name},\n' \
               f'My last name is: {self.lastname},\n' \
               f'and I\'m {self.age} old.'


# Student Class
class Student(Person):
    def __init__(self, name, lastname, age, student_id):
        Person.__init__(self, name, lastname, age)
        self.student_id = student_id

    # Method
    def message(self):
        return f'My name is: {self.name},\n' \
               f'My last name is: {self.lastname},\n' \
               f'and I\'m {self.age} old.\n' \
               f'My student id is: {self.student_id}'


print('***************Person Class****************')
# Instance/Object of the Person class
person_obj1 = Person('Jason', 'Mamoa', 18)
print(person_obj1.message())

print('**************Student Class*******************')
student_obj1 = Student('Rick', 'Sekuloski', 30, 12243434)
print(student_obj1.message())
