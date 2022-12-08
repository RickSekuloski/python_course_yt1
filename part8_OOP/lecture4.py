'''
Description:
The program should have two classes.
The first class will be called Person and the second class will be called Employee.
You will need to guess their relationship, so you can write the inheritance correctly.
The person class will have the following attributes:
• name
• dob (date of birth)
• id_number
In the person class, you should have an info() method that will print all of the Person details in a new line.
The class Employee should be able to use all of the attributes and methods from the parents class,
but it should also have new attributes:
• salary
• position
The employee class will have its own info() method with the same name as from the Person class, so it can print
the parent class details plus the new Employee details as well (method overriding).
In the end, you need to create an instance of the class Person and call the info method then create
another instance of the Employee class and call the info() method.
'''


# Parent Class
class Person(object):
    def __init__(self, name, dob, id_number):
        self.name = name
        self.dob = dob
        self.id_number = id_number

    # method
    def info(self):
        print(f'name: {self.name}\n'
              f'dob: {self.dob}\n'
              f'id:{self.id_number}')


# Child Class
class Employee(Person):
    def __init__(self, name, dob, id_number, salary, position):
        Person.__init__(self, name, dob, id_number)
        self.salary = salary
        self.position = position

    def info(self):
        print(f'name: {self.name}\n'
              f'dob: {self.dob}\n'
              f'id:{self.id_number}\n'
              f'salary: {self.salary}\n'
              f'position: {self.position}')


print('*********** Person ***********')
# Instance of the Person Class
person_obj = Person('Andy', '29/09/1999', 1224343)
person_obj.info()
print('*********** Employee ***********')
# Instance of the Employee Class
employee_obj = Employee('James', '19/09/2002', 13334435, 7000, 'developer')
employee_obj.info()