# Write a script prodby2.py that asks the user to enter a positive integer n and that will calculate and
# print the product of the odd integers from 1 to n (or from 1 to n-1 if n is even).

n = int(input("Enter a positive integer n: "))
product = 1

for i in range(1, n + 1, 2):
    product *= i

print(product)