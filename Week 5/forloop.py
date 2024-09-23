# Write a for loop that prints all characters of a string my str vertically in the console. Do two versions:
# one that will iterate through the elements of my str themselves, and one that will iterate through the
# indexes of my str (remember that a string is just a sequence of characters, and you can access the
# element located at index i of a sequence X by simply writing X[i] - careful: the counting starts at 0 !
# - and the length of the sequence X by writing len(X))

myStr = input("Enter a string here: ")

#Element method
for element in myStr:
    print(element)

for i in range(0, len(myStr)):
    print(myStr[i])