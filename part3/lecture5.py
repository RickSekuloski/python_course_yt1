# Lecture 5 from part3 ----Useful Tips for Lists----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.

# Useful Tips for Lists

# reverse the entire string using slicing
num_list = [3, 6, 7, 1, 5, 2, 4]
print(num_list[::-1])

#copy a list using slicing
num_list = [3, 6, 7, 1, 5, 2, 4]
new_list1 = num_list[:]
print(new_list1)

# generate new list using range function
num_list2 = list(range(0,50))
print(num_list2)

#.join()
usernames = ['andy','carol', 'steve', 'jason']
joined_usernames = ', '.join(usernames)
print(joined_usernames)

#list unpacking

andy, carol, steve, jason = ['andy','carol', 'steve', 'jason']
print(andy)
print(carol)
print(steve)
print(jason)
andy, carol, *rest = ['andy','carol', 'steve', 'jason']
print(andy)
print(carol)
print(rest)
