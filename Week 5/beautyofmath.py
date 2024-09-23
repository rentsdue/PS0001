# Write a script beautyofmath.py that produces the following output. The script should iterate from 1
# to 9 to produce the expressions on the left, perform the specified operation to get the results shown on
# the right, and print exactly in the format shown here. (while not necessarily needed, you can convert
# an integer X into a string using str(X), and you can concatenate two strings a and b by simply using
# the addition operator a+b)

leftNum = 0

for i in range(1, 10):
    leftNum = leftNum * 10 + i
    rightNum = leftNum * 8 + i
    print(leftNum, "x 8 + 1 =", rightNum)