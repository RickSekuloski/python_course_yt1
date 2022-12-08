# Super() function

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
        super().__init__(name, dob, id_number)
        # Person.__init__(self, name, dob, id_number)
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
