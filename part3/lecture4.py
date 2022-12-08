# Lecture 4 from part3 ----List Methods----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.
# Lists Methods
my_list = ['one', 'two', 'three']
#1) append()
my_list.append('four')
print(my_list)
#2) insert()
my_list.insert(4, 'five')
print(my_list)
#3) extend()
my_list.extend(['six', 'seven'])
print(my_list)
#4) pop()
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)
#5) remove()
print(my_list.remove('four'))
print(my_list)
#6) clear()
my_list.clear()
print(my_list)
#7) index()
new_list = ['one', 'two', 'three', 'four', 'five']
print(new_list.index('three'))
print(new_list.index('three', 0, 3))
# print(new_list.index('three', 0, 2))
#8) count()
my_list1 = ['one', 'two', 'three', 'one', 'four']
print(my_list1.count('one'))
#9) sort()
numbers_list = [3, 6, 7, 1, 5, 2, 4]
numbers_list.sort()
print(numbers_list)
#10) copy()
numbers_list = [3, 6, 7, 1, 5, 2, 4]
new_list = numbers_list.copy()
print(new_list)
#11) reverse()
numbers_list2 = [3, 6, 7, 1, 5, 2, 4]
numbers_list2.reverse()
print(numbers_list2)
#combine different list methods
numbers_list3 = [3, 6, 7, 1, 5, 2, 4]
numbers_list3.sort()
numbers_list3.reverse()
print(numbers_list3)