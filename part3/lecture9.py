# Tuples in Python - Data Type

new_tuple = (1, 2, 3)
# lists use []
# dict use {}
print(new_tuple)
print(new_tuple[0])
# new_tuple[0] = 0
print(len(new_tuple))

# Tuples and Dictionaries
car = {
    'brand' : 'Toyota',
    'gen' : [1, 2, 3, 4],
    'year': 2023,
    ('car','suv'): '2.5 engine'
}
print(car.items())
print(car['car','suv'])

# tuple slicing
new_tuple1 = (1, 2, 3, 4)
new_tuple2 = new_tuple1[0:2]
print(new_tuple2)

# unpacking
new_tuple3 = (1, 2, 3, 4, 5, 6)
one,two,three, *rest = new_tuple3
print(one)
print(two)
print(three)
print(rest)
rest[2] = 7
print(rest)