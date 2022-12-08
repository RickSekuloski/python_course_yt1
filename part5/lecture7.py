# Positional and Keyword Arguments
def display_details(name, lname, age):
    print(f'Hi there {name} {lname}. Are you {age} years old?')
# Positional arguments
display_details('Rick','Sekuloski',33)
display_details('Rick',33,'Sekuloski')
#Keyword arguments
display_details(name='Rick',lname='Sekuloski',age=33)
display_details(name='Rick',age=33,lname='Sekuloski')