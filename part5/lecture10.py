# Nested Functions
def outer_fn(num1, num2):
    def inner_fn(n1, n2):
        return n1 + n2
    total = inner_fn(num1, num2)
    return total

result = outer_fn(1, 3)
print(result)
    