# Iterables
'''
These are iterables:
- Strings
- Sets
- Tuples
- Dictionaries
- Lists

Iterated - looped over
'''

# Loop over a Dictionary
car_dict = {
    'brand': 'Tesla',
    'model': 'Model Y',
    'year': 2023,
    'engine': 'Electric'
}
print('---------For loop--------')
# for loop
for item in car_dict:
    print(item)
    
print('---------Items method--------')
# items() method

for item in car_dict.items():
    print(item)

print('---------Values method--------')
# values() method

for item in car_dict.values():
    print(item)

print('---------Keys method--------')
# keys() method
for item in car_dict.keys():
    print(item)

print('---------Unpacking --------')
for item in car_dict.items():
    key, value = item
    print(key, value)

print('---------For loop updated syntax--------')
# for loop
for key,value in car_dict.items():
    print(key,value)