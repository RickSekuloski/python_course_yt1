# Python Nested Loops
'''
for val in sequence
    for val in sequence
        ......
'''
numbers1 = [1, 2, 3]
letters1 = ['a', 'b']

for item in numbers1:
    print(item)
    for letter in letters1:
        print(letter)

print('Outisde of the for-loop')

# Nested if-statments

grade = 51

if grade >= 49:
    if grade >= 85:
        print('HD')
    elif grade >= 75 and grade <= 84:
        print('D')
    elif grade >= 65 and grade <= 74:
        print('Cr')
    elif grade >= 50 and grade <= 64:
        print('P')
else:
    print('F')
'''
 HD	 85% and above (High Distinction)
 D	 75–84% (Distinction)
 Cr  65–74% (Credit)
 P	 50–64% (Pass)
 F	 49% and under (Fail)
'''