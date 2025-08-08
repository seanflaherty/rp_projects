arr = [2, 3, 4, 5]

def square(func, it):
    new = []
    for i in it:
        n = func(i)
        new += [n]

    print(*new) #using the * to unpack the result from the lambda
                #into a list (or you can cast it as a list.)

square(lambda x: x ** 2, arr)