# Local and Function scope
x = 1
def trick_me(x):
    # global x
    # x = x + 4
    x += 4
    return x

print(trick_me(x))