# MRO - Method Resolution Order
# Class A
class A:
    def __init__(self, name='A'):
        self.name = name

    def info(self):
        return self.name


# Class B That Inherits from Class A
class B(A):
    pass


# Class C That Inherits from Class A
class C(A):
    def __init__(self, name='C'):
        self.name = name

    def info(self):
        return self.name


# Class D That Inherits from Class B and Class C
class D(B, C):
    pass


# instance of class D
d_object = D()
print(d_object.info())

# MRO
print(D.mro())
