# Lecture 2 from part3 ----List slicing----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.
# List slicing
# listname[start:stop]
# with step-over listname[start:stop:step]

#list slicing
my_list = [1, 2, 3, 4, 5, 6]
print(my_list[0:3])
#with stepover
my_list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list3[0::2])

# Lists are mutable
my_list3[0] = -1
print(my_list3)

#copy list
string_list = ['one', 'two', 'three']
string_list_copy = string_list[0:]
print(string_list_copy)
string_list_copy[1] ='2'
print(string_list_copy)
print(string_list)

# don't copy lists like this
string_list1 = ['one', 'two', 'three']
string_list_copy1 = string_list1
print(string_list_copy1)
string_list_copy1[0] = 'none'
print(string_list_copy1)
print(string_list1)