# is operator VS == opertor

# ==
print(True == 1)
print(True == bool(1))
#same as this:
print(True == True)

print('' == 1)
# print(False == 1)
# print(False == bool(1))
# print(False == True)

# is 
print(True is True)
print([1,2] is [1,2])

list1 = [1,2]
list2 = list1
print(list1 is list2)
list2.append(3)
print(list1)