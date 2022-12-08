# Lecture 2 from part2 ---- Str - Type Casting or Type conversion ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.

my_name = 'Keanu'
my_lastname = "Reeves"
print(my_name)
print(my_lastname)
print(type(my_name))

#multi-line string
text = '''
first line
second line
third line
'''
print(text)

full_name = my_name + ' ' + my_lastname
print(full_name)

hello = 'Hi'
# to string
five = str(5)

message = hello + five
print(message)

#Type casting or Type conversion
#explicit type casting
print(type(five))
#int
num1 = int('5')
num2 = 4
print(type(num1))
print(num1 + num2)

#float
num3 = float('5.5')
num4 = 4.3
print(type(num3))
print(num3 + num4)