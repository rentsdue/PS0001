import math

def funcA(x):
    if x <= 0:
        return x + 2
    else:
        return x / math.sqrt(x)

def funcB(x):
    return 2 * x ** 6 + 3 * x - 2

def funcC(x):
    if x < -6:
        return -6
    elif -6 <= x < 3:
        return -x
    else:
        return 0

def menu_func():
    function = input("")