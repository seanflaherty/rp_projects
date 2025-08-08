# factory function
def root_calculator_factory(root_degree):
    def root_calculator(number):
        return pow(number, 1 / root_degree)
    return root_calculator

square_root = root_calculator_factory(2)
print(square_root(49))

cube_root = root_calculator_factory(3)
print(cube_root(125))