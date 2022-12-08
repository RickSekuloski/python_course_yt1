# Lecture 10 from part2 ----Functions and Methods----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.
# Functions and Methods

# Python built-in functions
# 1) len()
text = 'A string'
print(len(text))
print(len('A string'))

#2) round(number, ndigits)
print(round(4.8888))

# Methods

# String Methods
text1= 'A string'
# 1) Upper()
# dot notation
result1 = text1.upper()
print(result1)

# 2) Capitalize()
print('hi there'.capitalize())
# 3) Lower()
print('Hi There'.lower())
# 4) find()
result2 = 'My name is Rick, what is yours?'.find('is')
print(result2)
# 5) replace()
#repace(oldvalue,newvalue)
original_string = 'My name is Rick, what is yours?'
result3 = original_string.replace('Rick','Mick')
print(original_string)
print(result3)
# 6) join()
result4 = '-'.join(['This','course','is', 'awesome!'])
print(result4)
