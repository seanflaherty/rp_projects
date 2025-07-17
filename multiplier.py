class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def __call__(self, number):
        return (number * self.multiplier)
    
doubler = Multiplier(2)
print(doubler(2))

tripler = Multiplier(3)
print(tripler(5))