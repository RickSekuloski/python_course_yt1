# Lecture 1 from part2 ---- Str - Strings another Data Type ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.

my_name = 'Keanu'
my_lastname = "Reeves"
print(my_name)
print(my_lastname)
print(type(my_name))

# multi-line string
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