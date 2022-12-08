# Ninth Lecture from part1 ---- Float - Floating Point Number ----
# Important! if you want to run this lecture on replit.com
# you need to copy and paste the content into the main.py
# file and press the run button.

# Numbers with decimal part like 3.5, -6.3
m = 3.2
n = 1.7

print(m * n)

#type
print(type(n))


#Python Power Operator (**)

print(2 ** 3)
print(3 ** 3)

#Python Double Slash Operator - Floor Divison //

print( 5 // 4)


#Python Modulo (%)

print( 5 % 4)

#Operator Precedence
'''
ORDER OF PRECEDENCE
1) () brackets highest precedence
2) ** (power of)
3) *, /
4) -, +
(7 - 3)*2 + 2**2
'''
a = 7-3*2

'''
1) 3*2 => 6
2) 7 - 6 = 1
'''
print(a)

print((7 - 3)*2 + 2**2)

# Math Functions

#1) round() function
print(round(4.3))
print(round(4.6))

#2) abs() function

print(abs(-11))
print(abs(-11.55))