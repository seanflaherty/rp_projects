def print_with_counter():
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter = counter + 1
        print(*args, **kwargs)
    def get_counter():
        return counter
    inner.get_counter = get_counter
    return inner
    
print_ = print_with_counter()

print_("Python!")
print_("Python is great!")
print(print_.get_counter())