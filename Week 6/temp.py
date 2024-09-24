# Create a script temp.py that continues asking the user to enter temperatures in degrees Celsius and
# store them in a list L. The process stop when the user enters the character ’e’. Then, using list
# comprehension, generate a new list LT of tuples, where each tuple has two values, a temperature in
# Celsius and its corresponding temperature in Farenheit (you can use the formula F = 1.8C + 32).

temperatureList = []

while True:
    userInput = input("Please enter a temperature in degrees celsius - press \"e\" to stop the process: ")
    if userInput == "e":
        break
    else:
        celsius = float(userInput)
        temperatureList.append(celsius)

finalTempList = [(c, 1.8 * c + 32) for c in temperatureList]

print(finalTempList)