import math

# Testing class 
radiusString = input("Enter the radius of your circle: ")
print(type(radiusString))

radius = int(radiusString)
print(type(radius))
circumference = radius * 2 * math.pi
print("Circumference of a circle:" , circumference)
print(math.pi)

# Grade code
grade = int(input("Enter a grade: "))
if grade > 10 or grade < 0:
    print("Impossible")
elif grade >= 9:
    print("A")
elif grade == 8:
    print("B")
elif grade == 7:
    print("C")
elif grade == 6:
    print("D")
else:
    print("F")

# Quadratic formula question
a = float(input("Coefficient a: "))
b = float(input("Coefficient b: "))
c = float(input("Coefficient c: "))
discriminant = b ** 2 - (4 * a * c)
print(discriminant)

if discriminant < 0:
    print("No real roots for this equation")
elif discriminant == 0:
    print("Root: " + str(-b / (2 * a)))
else:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Roots:" , root1, " and " , root2)

# Imagine a user menu to order pizzas online. The user is first asked to choose between 3 different types
# of pizzas (margherita at S$15.5, marinara at S$17.5 and napoletana at S$18) and once the pizza type
# selected he is invited to type the amount of such pizzas he would like to order. Finally, the user is
# asked if he would like to stop the ordering. If not, then the menu comes back to asking to select the
# pizza

margherita = 15.5
noOfMargherita = 0
marinara = 17.5
noOfMarinara = 0
napoletana = 18
exitBool = True
noOfNapoletana = 0
totalPrice = 0

while (exitBool):
    pizzaType = int(input("Type of pizza you want: \n 1    2    3 \n"))
    pizzNum = int(input("Tell me how many pizzas you want: "))
    if pizzaType == 1:
        totalPrice += margherita * pizzNum
    elif pizzaType == 2:
        totalPrice += marinara * pizzNum
    elif pizzaType == 3:
        totalPrice += napoletana * pizzNum
    else:
        print("Bruh read the instructions lmao.")
    
    exitString = input("Do you want to exit? \n Type 'y' to exit, and 'n' to continue.")
    if exitString == 'y':
        exitBool = False
        print("The total price is: ", totalPrice)

# Write a Python program that takes as input 3 crime rate values and that outputs the average crime rate over the 3 values.

crimeRate1 = int(input("Year 1 crime rate: "))
crimeRate2 = int(input("Year 2 crime rate: "))
crimeRate3 = int(input("Year 3 crime rate: "))
avg = (crimeRate1 + crimeRate2 + crimeRate3) / 3
print("Average crime rate: ", avg)

# What is the output of the following algorithm, if the user inputs X = 35 and Y = 10 (assume that
# the user always inputs X > 0 and Y > 0) ? What is this algorithm computing ?

s = 0
x = 69
y = 10
while x - y >= 0:
    s += 1
    x -= y
print(s, x)

# # What is the output of the following algorithm, if the user inputs X = 3 and Y = 8 (assume that the
# # user always inputs X ≥ 0) ?
# # What is this algorithm computing ?
s = 1
x = int(input("X value: "))
y = int(input("Y value: "))
while x > 0:
    s *= y
    x -= 1
print(s)

