# Identity Operators
'''
is - operator will return true if both of the variables are the same object
is not - operator will return true if both variables are not
the same object
''' 
a = ['apple']
b = ['apple']
c = a
# is - operator examples
print( a is c )
print( a is b )
print( a == b )

# is not - operator examples

print ( a is not c )
print ( a is not b )
print ( a != b )