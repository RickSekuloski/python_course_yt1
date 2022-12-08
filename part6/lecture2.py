# Scope

#global scope
result = 10
print(result)

# block scope
def num_fun():
    num1 = 4
    return num1
    # print(result,  num1)


num1 = num_fun()
print(num1)

print('Guess the output')

x = 1
def trick_me(x):
    x = 4
    return x

print(x)
print(trick_me(104))