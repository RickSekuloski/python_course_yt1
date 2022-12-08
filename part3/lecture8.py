# Python IN Keyword
this_dictionary1 ={
    'car' : True,
    'brands' : ['Ford', 'Tesla', 'Rivian'],
    'year' : 2023
}
print('year' in this_dictionary1)
print('years' in this_dictionary1)
# Dictionary Methods

# 1) get() method
print(this_dictionary1.get('year'))
print(this_dictionary1.get('cars',['Not Found']))

# 2) keys() method
print(this_dictionary1.keys())
print('car' in this_dictionary1.keys())

# 3) values() method
print(this_dictionary1.values())

# 4) items() method
print(this_dictionary1.items())
# 5) clear() method
print(this_dictionary1.clear())
print(this_dictionary1)
# 6) copy() method
this_dictionary2 ={
    'car' : True,
    'brands' : ['Ford', 'Tesla', 'Rivian'],
    'year' : 2023
}
dict_copy = this_dictionary2.copy()
print(dict_copy)

# 7) pop() method
this_dictionary2.pop('year')
print(this_dictionary2)

# 8) popitem() method
this_dictionary2.popitem()
print(this_dictionary2)

# 9) update() method
print(dict_copy.update({'year':2024}))
print(dict_copy)

# 10) setdefault() method
year = dict_copy.setdefault('year')
print(year)