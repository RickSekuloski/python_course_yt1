# Python Loops
'''
for val in sequence
    <statement(s)>
'''

my_name = 'Jason'
for char in my_name:
    print(char)

# Iterate over list
list1 = [1, 3, 5, 7, 9]

for item in list1:
    print(item)
    
# Iterate over set
set1 = {'apple', 'banana', 'pineapple', 'strawberry'}
for item in set1:
    print(item)
    
# Iterate over tuple
tuple1 = {'tesla', 'ferrari', 'porsche', 'mercedes'}
for item in tuple1:
    print(item)
    
#calculate tips
tips = [22.70, 56.30, 49.50, 47.87, 90.90]
tips_sum = 0
for tip in tips:
    tips_sum += tip

print(tips_sum)