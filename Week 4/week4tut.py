# Write a Python script functions.py to compute the following expressions, assuming that the angles
# are in radian (by importing the math package, you have access to many math-related methods or
# attributes, such as math.sqrt() for square root, math.pi for pi value, math.e for e value, math.log()
# for logarithm, math.cos(), math.sin(), math.tan() for trigonometric functions, etc.):

import math
answer1 = ((math.e ** 1.4) + math.log(465 ** 2)) / (math.sqrt(2) + 14) + (12 / math.sqrt(math.e + 4))
answer2 = 2.6 ** 0.2 + (math.e ** - math.sqrt(43.3) / math.tan(276)) + 17 ** (-1 / 7)
answer3 = ((math.pi ** 3 - 5.6 ** 2 + 1) / (1.2 ** (math.pi / 2) - math.sin(43))) + (14.8 / 5) ** (math.pi - 1.8)
print(answer1)
print(answer2)
print(answer3)

# Write a script that tests whether the user can follow instructions. It prompts the user to enter the
# character ‘x’. If the user enters anything other than an ‘x’, it prints an error message - otherwise, the
# script does nothing.
word = input("Enter a word: ")
if word.lower() != "x":
    print("TYPE X!!!!!")

# Write a script to calculate the volume of a pyramid (rectangle base), which is 1/3 * base * height,
# where the base is length * width. Prompt the user to enter values for the length, width, and height,
# and then calculate the volume of the pyramid. When the user enters each value, he or she will then
# also be prompted for either ‘i’ for inches or ‘c’ for centimeters. (Note 2.54 cm = 1 inch). The script
# should print the volume in cubic inches.

print("This program will calculate the volume of a pyramid.")
length = float(input("Enter the length of the base: "))
unitOfLength = input("Is that i or c? ")
width = float(input("Enter the width of the base: "))
unitOfWidth = input("Is that i or c? ")
height = float(input("Enter the height: "))
unitOfHeight = input("Is that i or c? ")

if unitOfLength == "c":
    length /= 2.54

if unitOfWidth == "c":
    width /= 2.54

if unitOfHeight == "c":
    height /= 2.54

volume = length * width * height / 3

print("The volume of the pyramid is " , volume , " cubic inches.")

# In chemistry, the pH of an aqueous solution is a measure of its acidity. The pH scale ranges from 0
# to 14, inclusive. A solution with a pH of 7 is said to be neutral, a solution with a pH greater than 7
# is basic, and a solution with a pH less than 7 is acidic. Write a script that will prompt the user for
# the pH of a solution, and will print whether it is neutral, basic, or acidic. If the user enters an invalid
# pH, an error message will be printed.

pH = float(input("Enter the pH value of an aqueous solution: "))
if pH < 0 or pH > 14:
    print("Invalid pH Value! Please try again.")
elif 0 <= pH < 7:
    print("The solution is acidic.")
elif pH == 7:
    print("The solution is neutral.")
else:
    print("The solution is basic.")

# Write a script travel.py that will first prompt the user for a distance in kilometers (with error check
# that the input distance can’t be negative). Then, the script will print the cost of the travel by walking,
# by motorcycle, by car and by plane, knowing that:
#  walking, motor-cycle, car and plane travel cost 0, 0.22, 0.26 and 0.78 SGD per kilometer respectively;
#  walking can’t be done for more than 20 kilometers, motor-cycle travel can’t be done for more
# than 200 kilometers, car travel can’t be done for more than 800 kilometers, plane travel can’t be
# done for less than 100 kilometers

distance = float(input("Enter the distance in kilometer: "))
costOfCycle = 0.22 * distance
costOfCar= 0.26 * distance
costOfPlane = 0.78 * distance
if distance < 0:
    print("The input distance can't be negative")
else:
    if 0 <= distance <= 20:
        print("The cost by walking is free !")
        print("The cost by motorcycle is ", costOfCycle, " SGD.")
        print("The cost by car is ", costOfCar, " SGD.")
    else:
        print("Sorry, you can't get there by walking.")
        if distance <= 200:
            print("The cost by motorcycle is ", costOfCycle, " SGD.")
        else:
            print("You travel is too long to be done by motorcycle.")
        if distance <= 800:
            print("The cost by car is ", costOfCar, " SGD.")
        else:
            print("You travel is too long to be done by car.")
    if distance < 100:
        print("You travel is too short to be done by plane.")
    else:
        print("The cost by plane is ", costOfPlane, " SGD.")

# Write a script currency.py that will prompt the user for an amount in Singapore Dollars, and then
# to which foreign currency he would like to convert this amount (’E’ for Euros, ’U’ for US Dollars, ’J’
# for Japanese Yen). The script will then print the original amount and the converted amount. The
# output can look like this:

singaporeDollars  = float(input("Enter the amount in Singapore Dollars: "))
currency = input("Do you want to convert this amount in Euros (E), US Dollars (U) or Japanese Yen (J)? ")
if singaporeDollars < 0:
    print("Bro you can't input a negative number.")
else:
    if currency == "E":
        print(singaporeDollars, " Singapore Dollars equals", (singaporeDollars * 0.70), " Euros")
    elif currency == "U":
        print(singaporeDollars, " Singapore Dollars equals", (singaporeDollars * 0.77), " US Dollars")
    elif currency == "J":
        print(singaporeDollars, " Singapore Dollars equals", (singaporeDollars * 109.53) , "Yen")

# Write a script three func.py that first asks the user which one of the three functions he would like to
# compute (with an error check), then asks for an x value and finally returns the value of the function
# chosen on point x. By importing the math package, you have access to many math-related methods
# or attributes, such as math.sqrt() for square root.

x = float(input("Enter a value of x: "))
if x < -6:
    print("The answer is 6.")
elif -6 <= x < 3:
    print("The answer is: ", x * -1)
else:
    print("The answer is 0.")

# Write a script areaMenu.py that will print a list consisting of “cylinder”, “circle”, and “rectangle”. It
# prompts the user to choose one, and then prompts the user for the appropriate quantities (e.g., the
# radius of the circle) and then prints its area. If the user enters an invalid choice, the script simply prints
# an error message. By importing the math package, you have access to the value of pi via math.pi. The
# script should use a nested if-else statement to accomplish this. Here are two examples of running
# it (units are assumed to be inches)

shape = input("Menu\n1. Cylinder\n2. Circle\n3. Rectangle\nPlease choose one: ")
if shape == "1":
    radiusCylinder = float(input("Enter the radius of the cylinder: "))
    heightCylinder = float(input("Enter the height of the cylinder: "))
    print("The volume is: ", (radiusCylinder ** 2 * heightCylinder * math.pi))
elif shape == "2":
    radius = float(input("Enter the radius of the circle: "))
    print("The area is: ", (radius ** 2 * math.pi))
elif shape == "3":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print("The area is: ", (length * width))
else:
    print("Invalid response.")
