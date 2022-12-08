# Sets new Data Type / Data Structure
new_set = {1,2,3,4,5,6,7}
print(new_set)

# add method
new_set.add(8)
print(new_set)

#ACCESSING SET ITEMS
# new_set[0]
# IN Keyword
print(4 in new_set)
print(9 in new_set)

# set lenght
print(len(new_set))

# Generate a Set from a List
new_list = [1,2,3,4,5,6,7,7,6]
new_set = set(new_list)
print(new_set)

# Convert a Set to a List
new_set1 = {1,2,3,4,5,6,7,8}
new_list1 = list(new_set1)
print(new_list1)