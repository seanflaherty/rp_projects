def pack(f):
    def wrap(x): return (f(x), x)
    return wrap

@pack
def square(x): return x ** 2
print(square(3)[1])