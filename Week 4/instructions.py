# Write a script that tests whether the user can follow instructions. It prompts the user to enter the
# character ‘x’. If the user enters anything other than an ‘x’, it prints an error message - otherwise, the
# script does nothing.

def inputX():
    stringToInput = input("Input the character x: ")
    if stringToInput != "x":
        print("Bro, I literally said type the letter x.")

inputX()