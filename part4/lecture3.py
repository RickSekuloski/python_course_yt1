# Operators, Comparison Operators
x = 3
y = 4

#1) Equal operator ==
print(x == y)
#2) Greater than >
print(x > y)
#3) Less than <
print(x < y)
#4) Greater than or eqaul to >=
print(x >= y)
#5) Less than or equal to <=
print(x <= y)
#6) Not equal !=
print(x != y)
print('------------Logical Operators------------')
# Logical Operators
# and
# or
# not
a = 4
# 1) and
print (a > 3 and a < 10)
print (a > 3 and a > 10)
# 2) or
print (a > 3 or a > 10)
print (a < 3 or a > 10)
# 3) not
print (not(a > 3 or a > 10))

my_age = 16
# my_age = 15
is_licenced = True

if is_licenced and my_age>=16:
    print('Hop for a ride')
else:
    print('Sorry buddy I will drive tonight!')