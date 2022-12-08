# Truthy vs Falsy values
'''
Values that are evaluated to False are considered to be Falsy
Values that are evaluated to True are considered to be Truthy.
''' 

if 7 > 4:
    print('True')
else:
    print('False')

x = 10
if x:
    print('True')
else:
    print('False')
    
#Boolen Context
    
# • Constant False
print(bool(False))

# •	Constant None
print(bool(None))

# •	Zero (0) 
print(bool(0))

# •	Float 0.0
print(bool(0.0))

# •	Complex 0j
print(bool(0j))

# •	Empty list []
print(bool([]))

# •	Empty tuples ()
print(bool(()))

# •	Empty dictionaries {}

print(bool(({})))

# •	Empty Sets sets()
print(bool(({})))

# •	Empty strings “”
print(bool(("")))

# •	Empty range(0)
print(bool(range(0)))


# user registration

username = 'jane'
password = ''
email = 'jane@gmail.com'

if username and password and email:
    print('The user can be registered!')
else:
    print('Some of the fileds are empty, please fill them')
    












