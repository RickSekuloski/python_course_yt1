# Lecture 8 from part2 ---- Str - Strings are Immutable ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.
my_name = 'Rick S'
print(my_name[0:4])
print(my_name[0:6])

# String Slicing with stepover
# [start:stop:stepover]
numbers = '012345678'
print(numbers[0:9:2])
print(numbers[1:])
print(numbers[:4])
print(numbers[::1])
print(numbers[::2])
print(numbers[-1])
print(numbers[::-1])

# Strings are Immutable
my_text = 'James'
print(my_text)
# my_text = 'Andy'
# print(my_text)
my_text[0] = 'K'
print(my_text)