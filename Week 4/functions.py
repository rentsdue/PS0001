# Write a Python script functions.py to compute the following expressions, assuming that the angles
# are in radian (by importing the math package, you have access to many math-related methods or
# attributes, such as math.sqrt() for square root, math.pi for pi value, math.e for e value, math.log()
# for logarithm, math.cos(), math.sin(), math.tan() for trigonometric functions, etc.):

import math

#Expression a
answerA = (math.e ** 1.4 + math.log(465 ** 2)) / (math.sqrt(2) + 14) + (12 / math.sqrt(math.e + 4))

#Expression b
answerB = 2.6 ** 0.2 + (math.e ** (-math.sqrt(43.3)) / math.tan(276)) + 17 ** (-1 / 7)

#Expression c
answerC = (math.pi ** 3 - 5.6 ** 2 + 1) / (1.2 ** (math.pi / 2) - math.sin(43)) + (14.8 / 5) ** (math.pi - 1.8)

#Test answers:
print(answerA, answerB, answerC)