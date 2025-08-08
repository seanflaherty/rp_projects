def print_with_memory():    
    record = []

    def inner(data):
        print(data)
        record.append(data)

    return inner

print_ = print_with_memory()

print_("Python!")
print_("Python is great!")
