# Functions, Function Arguments and Parameters
'''
Key Terms:
Function declaration / defining a function
Function call / Function Invocation
Function Parameters
Function Arguments
'''

# function
def hi_function():
    print('Hi there')
    
# call the function
hi_function()
# print(hi_function)

# Parameters and Arguments
#parameters
def hi_function1(name, lastname):
    print(f'Hi there {name}, {lastname}')
#arguments
name1 = 'Jason'
lastname1 = 'Mamoa'
hi_function1('Rick', 'Sekuloski')
hi_function1(name1, lastname1)

def calc_fun(n_list):
    sum_list = 0
    for item in n_list:
        sum_list += item
    print(sum_list)

num_list = [1, 2, 3]
num_list1 = [1, 2, 3, 4]
calc_fun(num_list)
calc_fun(num_list1)
# DRY - Do Not Repeat Yourself