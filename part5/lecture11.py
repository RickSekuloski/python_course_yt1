# Docstring
'''This is a string literal'''
def num_square(n1):
    '''This function takes a number as parameter and returns the square od that number'''
    return n1**2
result = num_square(4)
print(result)
# help(num_square)
help(num_square.__doc__)