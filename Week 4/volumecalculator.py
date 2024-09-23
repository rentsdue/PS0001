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