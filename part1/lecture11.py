# Lecture 11 from part1 ---- Variable Naming Rules ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.
# Sorry for spelling mistakes in the video!!!
'''
The variable name can only contain:
- letters a-z or A-Z
- numbers
_ underscore
'''

user_email = 'r@gmail.com'
user_Email = 'r@gmail.com'
userEmail = 'r@gmail.com'
user_email1 = 'r@gmail.com'
# Invalid variable names

'''
- The first character cannot be a number
'''
# 1st_number = 1
# print(1st_number)

# Snake Case, Camel Case

# Camel case
firstName = 'Rick'
# snake case
first_name ="Jason"
# help('keywords')

# await = 'one'

'''
Reassign variables to a new values
'''
num1 = 10
print(num1)
num1 = 12.5
print(num1)
num2 = num1
print(num2)

# Constants in Python
PI = 3.14
EARTH_GRAVITY = 9.807
print(PI)
print(EARTH_GRAVITY)
PI = 3.15
print(PI)