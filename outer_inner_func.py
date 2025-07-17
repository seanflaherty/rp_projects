def outer_func():
    name = "Pythonista"
    #def inner_func():
    #    print(f"Hello, {name}!")
    #return inner_func
    return lambda: print(f"Hello, {name}!")

greeter = outer_func()

greeter()