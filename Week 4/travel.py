# Write a script travel.py that will first prompt the user for a distance in kilometers (with error check
# that the input distance can’t be negative). Then, the script will print the cost of the travel by walking,
# by motorcycle, by car and by plane, knowing that:
#  walking, motor-cycle, car and plane travel cost 0, 0.22, 0.26 and 0.78 SGD per kilometer respectively;
#  walking can’t be done for more than 20 kilometers, motor-cycle travel can’t be done for more
# than 200 kilometers, car travel can’t be done for more than 800 kilometers, plane travel can’t be
# done for less than 100 kilometers

distance = float(input("Enter the distance in kilometer: "))
motorcycleCost = 0.22
carCost = 0.26
planeCost = 0.78

#Print cost of travel:
if distance < 0:
    print("Error: Distance cannot be negative as it isn't a vector!")
elif 0 <= distance <= 20:
    print("The cost by walking is free !")
    print("The cost by motorcycle is ", distance * motorcycleCost, " SGD")
    print("The cost by car is ", distance * carCost, " SGD")
    print("You travel is too short to be done by plane")
elif 20 < distance < 100:
    print("You travel is too long to be done by walking")
    print("The cost by motorcycle is ", distance * motorcycleCost, " SGD")
    print("The cost by car is ", distance * carCost, " SGD")
    print("You travel is too short to be done by plane")
elif 100 <= distance <= 200:
    print("You travel is too long to be done by walking")
    print("The cost by motorcycle is ", distance * motorcycleCost, " SGD")
    print("The cost by car is ", distance * carCost, " SGD")
    print("The cost by plane is ", distance * planeCost, " SGD")
elif 200 < distance <= 800:
    print("You travel is too long to be done by walking")
    print("You travel is too long to be done by motorcycle")
    print("The cost by car is ", distance * carCost, " SGD")
    print("The cost by plane is ", distance * planeCost, " SGD")
else:
    print("You travel is too long to be done by walking")
    print("You travel is too long to be done by motorcycle")
    print("You travel is too long to be done by car")
    print("The cost by plane is ", distance * planeCost, " SGD")
    