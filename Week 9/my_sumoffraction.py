def sumOfFraction(number):
    sum = 0
    for i in range(1, number + 1):
        sum += 1 / (i * (i + 1))
    return sum

print(sumOfFraction(2))