# While-loop
'''
while test_experssion
    <statement(s)>
'''
print('----------- while-loop-----------')
# while loop
num = 10
sum = 0
# counter
i = 1

while i <= num:
    print(i)
    # i = i + 1
    #sum = sum + i
    sum += i
    i += 1

print(sum)
print('----------- break the loop-----------')
#break from the loop
while i <= num:
    print(i)
    # i = i + 1
    #sum = sum + i
    sum += i
    if (i == 7):
        break
    i += 1

print(sum)
print('----------- while-else-----------')
#while-else
while i <= num:
    print(i)
    # i = i + 1
    #sum = sum + i
    sum += i
    i += 1
else:
    print('This is printed when the condition becomes false')

print(sum)