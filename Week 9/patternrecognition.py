def my_add2(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum

print(my_add2(4)) # Test statement


def my_add3(start, end, step):
    sum = 0
    for i in range(start, end + 1, step):
        sum += i
    return sum

# start = int(input("Enter a starting number: "))
# end = int(input("Enter an ending number: "))
# step = int(input("Enter the common difference: "))
# print(my_add3(start, end, step))

# A number sequence is below:
# {0, 3, 8, 15, 24, 35, 48, … }
# Analyse the pattern of this number sequence and write a program to calculate the sum of first 15 terms. (A bit
# more complicated pattern)

def addSequence(num):
    sum = 0
    for i in range(0, num):
        sum += (i ** 2 + i * 2)
    return sum

print(addSequence(15))

def numberOfDots(num):
    return 6 * num + 4

print(numberOfDots(30))

