# Lecture 5 from part2 ---- Str - Escape Characters ----
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

#implicit type casting
int_num1 = 10
float_num2 = 14.3
print('Data type of int_num1 is: ', type(int_num1))
print('Data type of float_num2 is: ', type(float_num2))

sum_numbers = int_num1 + float_num2
print('Total sum is: ', sum_numbers)
print('Data type of sum_numbers is: ', type(sum_numbers))

# Formatted Strings & How Strings are Stored in Memory
james = 'Daniel'
bond = 'Craig'
print(f'Dear {james} {bond}. We thank you for being 007 for so many years!')
print('Dear' + ' ' + james + ' ' + bond +
      '. We thank you for being 007 for so many years!')

my_name = 'Rick S'
print(my_name)
print(my_name[0])
print(my_name[4])
print(my_name[5])
# print(my_name[6])

# Escape Characters
text = 'I\'m James Bond'
print(text)
# James\Oliver\Thomas\Theodore
text2 = 'James\\Oliver\\Thomas\\Theodore'
print(text2)
# add a tab \t
text4 = 'This is without a tab'
text5 = '\t This is without a tab'
print(text4)
print(text5)

# add a new line \n
text6 = 'This is with a new line.\nNew line'
print(text6)