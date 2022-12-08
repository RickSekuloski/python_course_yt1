# Practice Time
# Exercise:
'''
We have learned about loops, operators
and conditionals. 
We have a dirty list. A dirty list is a
list that contains duplicate values. Make
a new list called clean_list without any
duplicate.
Tip1 - You can use one of the membership
operators.
Tip2 - You can use some of the built-in
Python functions and convert a list to
a particular data type that doesn't allowed
duplicate values
'''
dirty_list = [1,2,3,1,3,5,7,8,5,7,9,4,6,6,2,10,9,8]

# Solution 1 - membership operators not in
clean_list = []

#loop over the dirty list
for item in dirty_list:
    # print(item)
    if item not in clean_list:
        clean_list.append(item)

print(clean_list)

#Sulution 2
clean_set = set(dirty_list)
# print(clean_set)
clean_list = list(clean_set)
print(clean_list)