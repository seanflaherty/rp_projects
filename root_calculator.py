# closure
def make_root_calculator(root_degree, precision=2):
    def root_calculator(number):
        return round(pow(number, 1 / root_degree), precision)
    return root_calculator

square_root = make_root_calculator(2, 4)
print(square_root(42))

cubic_root = make_root_calculator(3)
print(cubic_root(42))

# using .__call__() method
class RootCalculator:
    def __init__(self, root_degree, precision=2):
        self.root_degree = root_degree
        self.precision = precision
    def __call__(self, number):
        return round(pow(number, 1 / self.root_degree), self.precision)

# make root calculator factory
#
print("Root Calculator Factory")
square_root = make_root_calculator(2, 4)
print(square_root(42))

cubic_root = make_root_calculator(3)
print(cubic_root(42))

# callable root calculator 
#
print("Callable RootCalculator")
square_root = RootCalculator(2, 4)
print(square_root(42))

cubic_root = RootCalculator(3)
print(cubic_root(42))