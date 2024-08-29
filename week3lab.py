import math

# 1. Type a simple printing command (for example display the string Singapore) and a simple addition command (for example add 12 to
# 15). Then, write the very same commands in a Python script (left panel) and run this script. Is there
# a difference ?

print("Singapore")
print(12+15)

# 2. Create a variable to store the atomic weight of Lithium (6.941)
atomicWeightLi = 6.941

# 3. Create a variable myage and store your age in it. Subtract 5 from the value of the variable. Add 8 to
# the value of the variable. Print the final value contained in myage.
myAge = 18
myAge -= 5
myAge += 8
print(myAge)

# 4. For each of the following commands, discuss what will be the outcome if they are executed by a Python
# interpreter, in this sequence (some will lead to errors, try to understand why):
# a = d (doesn't work as d is not defined)
# c = 10 
# a = c + 1
# a + c = c (LHS must have one variable only)
# 3 + a (isn't assigned to a variable)
# 7up = 10 (doesn't work since you can't have a number as the first letter in a variable)
# import = 1003 (can't use keywords)
# int = 500
# a ** 3 (isn't assigned to a variable)
# b = math.pi * c
# a, b, c = c, 1, a 
# b,c,a = a,b (not enough variables to unpack)
# c = b = a = 7
# print( A ) (A is not defined)
# print("b*b + a*a = c*c" )

# 5. The function help() is very useful when you want to find information about a function, a Python
# module, etc. To try it out, import the math module and use the function help to display informations
# about this module (help(math)). Then, using this help:
# (a) find and use the function from the math module that computes the hyperbolic sine of an angle in
# radian.
# (b) find and use the function from the math module that converts degrees into radians. Computes the
# sine of an angle in degree using that function and the math.sin function. Verify for example that
# with 90 degrees you obtain 1.

#Hyperbolic sine:
print(math.sinh(1))

#Degrees and radians
degree = 90
radian = math.radians(degree)
print(math.sin(radian))

# Each type in Python has specific attributes and methods that can be accessed using the dot (.)
# operator (to really simplify, you can view attributes and methods as functions). For example, create
# a variable my float and initialise it with a float value. On Spyder, you can see the list of attributes
# and methods available for that variable by typing my float. and then pressing the Tab key on your
# keyboard. Alternatively, you can list it by typing the command dir(my float). For example, the
# float type has a method as integer ratio() that decomposes the float as a ratio of two integers:
# (a) Explore the attributes and methods of the string type and then find and use the method that
# converts your string to uppercase.
# (b) What is the method split doing ?

myFloat = 0.25
print(dir(myFloat))
print(myFloat.as_integer_ratio())

myString = "Hello"
print(dir(myString))
print(myString.upper())
print(myString.split())

# 7. Create variables for the three resistors and store values in each, and then calculate the combined
# resistance
r1 = 3
r2 = 5
r3 = 6
totalResistance = 1 / ((1 / r1) + (1 / r2) + (1 / r3))

# 8. A farmer grows tomatoes and carrots and sells them at a market. Currently the tomato price per kilo
# is 3.29 SGD, and the carrots can be sold at 1.8 SGD per kilo. The farmer produced 123kg of tomatoes
# and 247kg of carrots. In a Python script farmer.py, assign the prices to variables named tomato price
# and carrot price and calculate the following by typing one command (aka a single line):

tomatoPrice = 3.29
carrotPrice = 1.8
tomatoesProduced = 123
carrotsProduced = 247

# (a) Compute the amount of money received by the farmer if he sells all its tomatoes and carrots
totalMoneyA = tomatoPrice * tomatoesProduced + carrotPrice * carrotsProduced

# (b) Compute the amount of money received by the farmer if he sells 87% of its tomatoes and 67% of
# its carrots
totalMoneyB = tomatoPrice * tomatoesProduced * 0.87 + carrotPrice * carrotsProduced * 0.67

# (c) The farmer has to pay 15% tax on his earnings from (b). Compute the amount of money received
# by the farmer after tax
totalMoneyC = 0.85 * totalMoneyB

# (d) Compute the same as (c), and round the total cost to the nearest dollar.
round(totalMoneyC)

# 9. Create variables for the temperature and wind speed, and then using this formula calculate the
# WCF.
temperature = 3
windSpeed = 3
wcf = 35.7 + 0.6 * temperature - (35.7 * windSpeed ** (0.16)) + 0.43 * temperature * windSpeed ** 0.16