# First Class
class First:
    pass


# Second Class
class Second:
    pass


# Third Class
class Third:
    pass


# Fourth Class
class Fourth (First, Second):
    pass


# Fifth Class
class Fifth (Second, Third):
    pass


# Sixth Class
class Sixth (Fifth, Fourth, Third):
    pass


# Print the algorithm Order
print(Sixth.mro())