max_ = "I was defined in the global scope!"

def outer_function():
    # max_ = "I'm in the outer function."
    def inner_function():
        max_ = "I'm from the inner function."
        print(max_)
    inner_function()
outer_function()