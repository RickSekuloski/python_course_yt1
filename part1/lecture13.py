# Lecture 12 from part1 ---- Expressions and Statements ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.

current_year = 2023
year_born = 1990
user_age = current_year - year_born
print(user_age)

# Augmented assignment operator
num1 = 30
num2 = 10
#num1 = num1 + num2


'''
+=, Addition and Assignment
-=, Subtraction and Assignment
*=, Multiplication and Assignment
/=, Division and Assignment
//=, Floor Division and Assignment
**=, Power and Assignment
%=, Modulo and Assignment

'''




# Addition & Assignment
# num1 = num1 + num2
num1 += num2
print(num1)
# Output: 40

num1 = 30
num2 = 10
# Subtraction & Assignment
num1 -= num2
print(num1)
# Output: 20


num1 = 30
num2 = 10
# Multiplication & Assignment
num1 *= num2
print(num1)
# Output: 300


num1 = 30
num2 = 10
# Division & Assignment
num1 /= num2
print(num1)
# Output: 3.0


num1 = 30
num2 = 10
# Floor Division & Assignment
num1 //= num2
print(num1)
# Output: 3


num1 = 30
num2 = 10
# Power & Assignment
num1 **= num2
print(num1)
# Output: 590490000000000

num1 = 30
num2 = 10

# Modulo & Assignment
num1 %= num2
print(num1)
# Output: 0