import numpy as np

myArray = np.loadtxt("fertility.txt")
year = 1960

#Increasing years pairs:
print("Increasing years pairs: ")
for i in range(0, len(myArray) - 1):
    year += 1
    
    if myArray[i] < myArray[i + 1]:
        print(year - 1 , "to", year)

#Calculate Average
sum = 0
for num in myArray:
    sum += num
average = sum / len(myArray)
print("Average fertility: ", average)

#Number of fertility higher than average
highCount = 0
for num in myArray:
    if (num > average):
        highCount += 1
print("Number of fertility higher than average:", highCount)