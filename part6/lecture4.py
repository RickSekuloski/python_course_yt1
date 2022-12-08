# nonlocal keyword

def outer_fn():
    username = 'John'
    def inner_fn():
        nonlocal username
        username = 'Tony'
    inner_fn()
    return username

print(outer_fn())