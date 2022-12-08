# Code Introspection
'''
Code introspection is the ability to examine classes,
functions and keywords to know what they are, what they
do and what they know.

Few built-in functions in Python:

'''
# 1 type()
str_obj = 'Hi'
list_obj = [1, 2, 3, 4]
int_obj = 10
float_obj = 11.1
dict_obj = {
    'type': 'dictionary'
}
print(type(str_obj))
print(type(list_obj))
print(type(int_obj))
print(type(float_obj))
print(type(dict_obj))

# 2 dir()
print('-------------- DIR method ------------')
print(dir(dict_obj))
print('-------------- STR method ------------')
# 3 str()
list_obj1 = [1, 2, 3, 4]
print(type(list_obj1))
# convert List to a String
print(type(str(list_obj1)))

# 4 id()
x = [1, 2, 3, 4, 5, 6]
# get the ID from a Object
print(id(x))
# You can read more about other built-in functions:
'''
https://docs.python.org/3/library/functions.html
'''
