def my_add2(n):
    sum = 0
    for i in range(0, n + 1):
        sum += i
    return sum

print(my_add2(4)) # Test statement


def my_add3(start, end, step):
    numTerms = ((end - start) / step) + 1
    return (numTerms / 2 ) * (start + end)

start = int(input("Enter a starting number: "))
end = int(input("Enter an ending number: "))
step = int(input("Enter the common difference: "))
print(my_add3(start, end, step))