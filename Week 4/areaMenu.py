# Write a script areaMenu.py that will print a list consisting of “cylinder”, “circle”, and “rectangle”. It
# prompts the user to choose one, and then prompts the user for the appropriate quantities (e.g., the
# radius of the circle) and then prints its area. If the user enters an invalid choice, the script simply prints
# an error message. By importing the math package, you have access to the value of pi via math.pi. The
# script should use a nested if-else statement to accomplish this. Here are two examples of running
# it (units are assumed to be inches)

import math

shape = input("Menu\n1. Cylinder\n2. Circle\n3. Rectangle\nPlease choose one: ")

if shape == "1":
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    volume = radius ** 2 * math.pi * height
    print("The volume is", volume)
elif shape == "2":
    radius = float(input("Enter the radius of the circle: "))
    area = radius ** 2 * math.pi
    print("The area is", area)
elif shape == "3":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area is", area)
