# Mammal - Parent Class

class Mammal:
    def __init__(self, name):
        self.name = name

    # eat Method
    def eat(self):
        print(f'{self.name} eats different types of foods!')

    # walk Method
    def walk(self):
        if self.name != 'Bat':
            print(f'{self.name} can walk.')
        else:
            print(f'The {self.name} is the only mammal that can fly!')


# Dog - Child class

class Dog(Mammal):
    def __init__(self, name, breed, legs, age):
        Mammal.__init__(self,name)
        self.breed = breed
        self.age = age
        self.legs = legs

    # eat Method
    def eat(self):
        print(f'{self.name} eats only dog food!')

    # details method
    # eat Method
    def details(self):
        print(f'The {self.name} is a {self.breed} \n'
              f'and like all other dogs have {self.legs} legs\n'
              f'and he is {self.age} years old.')


print('************* Mammal ***********')
mammal_obj1 = Mammal('Elephant')
mammal_obj1.eat()
mammal_obj1.walk()

mammal_obj2 = Mammal('Bat')
mammal_obj2.eat()
mammal_obj2.walk()
print('************* Dog ***********')
dog_obj1 = Dog('Ben', 'labrador', 4, 7)
dog_obj1.eat()
dog_obj1.walk()
dog_obj1.details()