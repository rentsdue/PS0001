
# Write a script threefunc.py that first asks the user which one of the three functions he would like to
# compute (with an error check), then asks for an x value and finally returns the value of the function
# chosen on point x. By importing the math package, you have access to many math-related methods
# or attributes, such as math.sqrt() for square root.

import math

def functionA(num):
    if num <= 0:
        return num + 2
    else:
        return num / math.sqrt(num)

def functionB(num):
    return 2 * num ** 6 + 3 * num - 2

def functionC(num):
    if num < -6:
        return 6
    elif -6 <= num < 3:
        return -num
    else:
        return 0

x = float(input("Enter a value of x: "))
choosefunction = input("Choose function A (type \"A\"), function B (type \"B\"), or function C (type \"C\"),")

if choosefunction == "A":
    print(functionA(x))
elif choosefunction == "B":
    print(functionB(x))
elif choosefunction == "C":
    print(functionC(x))
else:
    print("Error - invalid error inputted.")