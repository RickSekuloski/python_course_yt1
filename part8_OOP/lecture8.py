# Multiple Inheritance
# Father Class
class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(f'Name: {self.name}')

    def get_age(self):
        print(f'Age: {self.age}')


# Mother class
class Mother:
    def __init__(self, name, eyes):
        self.name = name
        self.eyes = eyes

    def get_name(self):
        print(f'Name: {self.name}')

    def get_eyes(self):
        print(f'Color of eyes: {self.eyes}')


class Child(Father, Mother):
    def __init__(self, name, personality, gender, age, eyes):
        # Father init
        Father.__init__(self, name, age)
        Mother.__init__(self, name, eyes)
        self.name = name
        self.personality = personality
        self.gender = gender

    def child_info(self):
        print(f'Name: {self.name}\n'
              f'Last name: {self.personality}\n'
              f'gender: {self.gender}\n')


# child object
morgan = Child('Morgan', 'cheeky', 'male', 3, 'Blue')
morgan.child_info()
morgan.get_name()
morgan.get_age()
morgan.get_eyes()

