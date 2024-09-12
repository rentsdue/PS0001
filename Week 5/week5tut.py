# Write a for loop that prints all characters of a string my str vertically in the console. Do two versions:
# one that will iterate through the elements of my str themselves, and one that will iterate through the
# indexes of my str (remember that a string is just a sequence of characters, and you can access the
# element located at index i of a sequence X by simply writing X[i] - careful: the counting starts at 0 !
# - and the length of the sequence X by writing len(X))

import math
myStr = input("Enter a string here: ")

#Element method
for char in myStr:
    print(char)

#Index method:
for i in range(0, len(myStr)):
    print(myStr[i])

# Write a script prodby2.py that asks the user to enter a positive integer n and that will calculate and
# print the product of the odd integers from 1 to n (or from 1 to n-1 if n is even).

number = int(input("Choose an integer: "))
product = 1
for i in range(1, number + 1, 2):
    product *= i
print(product)

# Write a script beautyofmath.py that produces the following output. The script should iterate from 1
# to 9 to produce the expressions on the left, perform the specified operation to get the results shown on
# the right, and print exactly in the format shown here. (while not necessarily needed, you can convert
# an integer X into a string using str(X), and you can concatenate two strings a and b by simply using
# the addition operator a+b)

leftNum = 0
for i in range(1, 10):
    leftNum = leftNum * 10 + i
    result = leftNum * 8 + i
    print(leftNum, "x 8 + ", i, " = " , result)

# Write a script approxe.py that will loop through values of n until the difference between the approximation and the actual value is less than 0.0001 (the actual value of e can be obtained in the math
# module). The script should then print out the built-in value of e
# −1 and the approximation to 4 decimal
# places, and also print the value of n required for such accuracy.

actualValue = 1 / math.e

n = 0
diff = 1
while diff >= 0.0001:
    n += 1
    approxValue = (1 - 1 / n) ** n
    diff = actualValue - approxValue

print("The real value is ", actualValue, ", and the value of the approximation is", approxValue, " and the value of n is ", n)
