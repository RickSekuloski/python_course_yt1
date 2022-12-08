# *args, **kwargs
'''
*args - Non Keyword Argument
**kwargs - Keyword Argument
'''
def years_old(curr, dob):
    return curr - dob

age = years_old(2023, 1999)
print(age)

def addition_fn(*args, **kwargs):
    # print(*args)
    # print(args)
    # print(kwargs)
    result = 0
    for item in kwargs.values():
        result += item
    return sum(args) + 24

result = addition_fn(1, 2, 3, 4, 5, 6, n7=7, n8=8, n9=9)
print(result)