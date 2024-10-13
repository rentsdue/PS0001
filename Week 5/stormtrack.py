import numpy as np # imports the numpy module (very import package for scientific computing with Python)
my_array = np.loadtxt("Week 5/Text Files/stormtrack.txt")# loads the data into the array my array
winds = my_array [:,0] # variable winds is a sequence that contains the 1st column of the data
visibs = my_array [:,1] # variable visibs is a sequence that contains the 2nd column of the data

count = 0
i = 0
length = len(winds)

while count < 4 and i < length:
    if winds[i] >= 30 and visibs[i] <= 0.5:
        count += 1
    else:
        count = 0
    i += 1

if count == 4:
    print ("Blizzard conditions met")
else :
    print ("No blizzard this time !")
