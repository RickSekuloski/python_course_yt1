# Dunder/ Magic Methods


class Car(object):
    def __init__(self, color, make, year, size):
        self.color = color
        self.make = make
        self.year = year
        self.size = size
    def __str__(self):
        return f'{self.make}'

# Instance/Object of the class Car
bmw_car = Car('red', 'bmw', 2023, 'sedan')
list_obj = [1, 2, 3]
print(dir(bmw_car))
print(len(list_obj))
# call the dunder method __str__
print(bmw_car.__str__())
print(str(bmw_car))
