# The cost of manufacturing n units (where n is an integer) of a particular product at a factory is given by the equation:
# C(n) = 5n^2 − 44n + 11
# Write a script mfgcost.py that will:
#   prompt the user for the number of units n
#   call a function costn that will calculate and return the cost of manufacturing n units
#   print the result (the format must be exactly as shown below)
# Next, write the function costn, which simply receives the value of n as an input argument, and
# calculates and returns the cost of manufacturing n units.

def costN(n):
    return 5 * n ** 2 - 44 * n + 11

numberOfUnits = float(input("Enter the number of units: "))
print("The cost for", numberOfUnits, "units will be $", costN(numberOfUnits))



