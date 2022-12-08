# Control Structures in Python
print('---------------- if-statement ---------')
# if-statement
'''
if <expression>:
    <statement(s)>
'''
is_developer = True

if is_developer:
    print('Wow this must be exciting!')

print('Outside the if-statement body')
print('---------------- if-else statement ---------')
# if-else statement
'''
if <expression>:
    <statement(s)>
else:
    <statement(s)>
'''
is_developer = False

if is_developer:
    print('Wow this must be exciting!')
else:
    print('What is your profession then?')
print('Outisde the if-else statement')

print('---------------- elif ---------')
# elif statement
'''
if <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
elif <expression>:
    <statement(s)>
.
.
.
else:
    <statement(s)>
'''

is_developer = False
is_employed = True
if is_developer:
    print('Wow this is great!')
elif is_employed:
    print('Great at least you have a job :)')
    print('Today is hard to have a job')
else:
    print('What is your profession then?')

print('Outside of the elif-block')

x = 10
if x > 11:
    print('The value of x is greater than 11')
elif x > 5:
    print('The value of x is bigger then 5')
else:
    print('The value of x is undefined')