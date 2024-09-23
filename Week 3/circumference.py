# Testing class 
import math

radiusString = input("Enter the radius of your circle: ")
print(type(radiusString))
radius = int(radiusString)
print(type(radius))
def circumferenceCalculator(radius):
    circumference = radius * 2 * math.pi
    print("Circumference of a circle:" , circumference)
    print(math.pi)

circumferenceCalculator(radius)