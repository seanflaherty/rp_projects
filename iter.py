from itertools import takewhile
def infinite():
    i = 1
    while True:
        yield i
        i *= 2
print(list(takewhile(lambda x: x <= 10, infinite())))