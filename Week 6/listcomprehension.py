# 5. Transform these list comprehension statements into equivalent code using loops:
seven = [x for x in range (1 ,100) if x %7==0]
primes = [x for x in range (2 , 100) if sum ([float ( x / y ).is_integer () for y in range(2 , x )]) == 0]

print(seven)
print(primes)

newSeven = []
for i in range (1, 100):
    if i % 7 == 0:
        newSeven.append(i)

print(newSeven)

newPrimes = []

for x in range(2, 100):
    dummyList = []
    for y in range(2, x):
        if (float(x / y)).is_integer():
            dummyList.append(y)
    if sum(dummyList) == 0:
        newPrimes.append(x)

print(newPrimes)

# Transform these loops into an equivalent code using list comprehension:
squares = []
for x in range (10):
    squares.append(x**2)
print(squares)
    
combs = []
for x in [1 ,2 ,3]:
    for y in [3 ,1 ,4]:
        if x != y :
            combs.append((x, y))
print(combs)

squaresNew = [x**2 for x in range(10)]
print(squaresNew)
combsNew = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if (x != y)]
print(combsNew)

# Write a list comprehension that uses nested for-clauses to create a list L of 2-element tuples, containing
# all 36 different dice combinations from (1,1) to (6,6). Repeat the exercise, but this time generate only
# the 21 different unordered dice combinations from (1,1) to (6,6), in other words (1,2) and (2,1) are
# considered the same combination

diceCombos = [(x, y) for x in range(1, 7) for y in range(1, 7)]
diceCombosReduced = [(x, y) for x in range(1, 7) for y in range(1, 7) if x <= y]
print(diceCombos)
print(diceCombosReduced)
