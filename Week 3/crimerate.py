# Write a Python program that takes as input 3 crime rate values and that outputs the average crime rate over the 3 values.

def crimeRate(crimeRate1, crimeRate2, crimeRate3):
    avg = (crimeRate1 + crimeRate2 + crimeRate3) / 3
    return ("Average crime rate: ", avg)

crimeRate1 = int(input("Year 1 crime rate: "))
crimeRate2 = int(input("Year 2 crime rate: "))
crimeRate3 = int(input("Year 3 crime rate: "))
print(crimeRate(crimeRate1, crimeRate2, crimeRate3))

