# Write a script approxe.py that will loop through values of n until the difference between the approximation and the actual value is less than 0.0001 (the actual value of e can be obtained in the math
# module). The script should then print out the built-in value of e^ −1 and the approximation to 4 decimal places, and also print the value of n required for such accuracy.

import math

actual = 1 / math.e
difference = 1
n = 0

while difference > 0.0001:
    n += 1
    approximation = (1 - 1 / n) ** n
    difference = actual - approximation

print("The approximation is", approximation, ", the value of n required is", n, "and the actual value of 1/e is", actual)