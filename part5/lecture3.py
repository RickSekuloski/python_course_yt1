# Enumerate function
'''
enumerate()
'''
# Tuple
x = ('one', 'two', 'three')
y = enumerate(x)
# print(y)

# for item in y:
#     print(item)

for key,item in y:
    print(key, item)

# Strings
for key,item in enumerate('Rick'):
    print(key, item)

# Lists
for key,item in enumerate([1, 2, 3, 4]):
    print(key, item)