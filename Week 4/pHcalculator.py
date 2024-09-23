# In chemistry, the pH of an aqueous solution is a measure of its acidity. The pH scale ranges from 0
# to 14, inclusive. A solution with a pH of 7 is said to be neutral, a solution with a pH greater than 7
# is basic, and a solution with a pH less than 7 is acidic. Write a script that will prompt the user for
# the pH of a solution, and will print whether it is neutral, basic, or acidic. If the user enters an invalid
# pH, an error message will be printed.

testpH = float(input("Enter a pH value: "))
if testpH > 14 or testpH < 0:
    print("Invalid pH value. It must be within 0 to 14, inclusive.")
elif 0 <= testpH < 7:
    print("The solution is acidic.")
elif testpH == 7:
    print("The solution is neutral.")
elif 7 < testpH <= 14:
    print("The solution is basic.")