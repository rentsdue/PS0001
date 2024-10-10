import time

# 4. The Fibonacci numbers are the numbers of the following sequence of integer values:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
# The Fibonacci numbers are defined by:
# 𝐹𝑛 = 𝐹𝑛−1 + 𝐹𝑛−2,
# with 𝐹0 = 0 and 𝐹1 = 1.
# So the recursive function can be written based on the following:
# 𝑟𝑒𝑡𝑢𝑟𝑛 0 𝑖𝑓 𝑛 == 0
# 𝑟𝑒𝑡𝑢𝑟𝑛 1 𝑖𝑓 𝑛 == 1
# 𝑟𝑒𝑡𝑢𝑟𝑛 𝑓(𝑛) = 𝑓(𝑛 − 1) + 𝑓(𝑛 − 2) 𝑖𝑓 𝑛 > 1
# Write a Python script to calculate the Fibonacci numbers by using recursive function my_rfibo(n) and print the
# numbers.

def my_rfibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return my_rfibo(n - 1) + my_rfibo(n - 2)

list1 = []
for i in range(0, 12):
    list1.append(my_rfibo(i))

print(list1)


# 5. The computation of Fibonacci numbers can also be accomplished by non-recursive method. We can
# implement an iteration method to calculate Fibonacci numbers, because we know both the index number 𝑛
# and the formula. The procedure is below:
# 𝑟𝑒𝑡𝑢𝑟𝑛 0 𝑖𝑓 𝑛 == 0
# 𝑟𝑒𝑡𝑢𝑟𝑛 1 𝑖𝑓 𝑛 == 1
# 𝑢𝑠𝑒 𝑎 𝑓𝑜𝑟 𝑙𝑜𝑜𝑝 𝑡𝑜 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑡𝑒 𝑓(𝑛) = 𝑓(𝑛 − 1) + 𝑓(𝑛 − 2) 𝑖𝑓 𝑛 > 1
# Write a Python script to calculate the Fibonacci numbers by using an iterative function 𝑚𝑦_𝑖𝑓𝑖𝑏𝑜(𝑛) and print
# the numbers

def my_ifibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    
list2 = []
for i in range(0, 12):
    list2.append(my_ifibo(i))

print(list2)

# Measure CPU time
startTime1 = time.process_time()  
result1 = my_rfibo(10) 
endTime1 = time.process_time()   
cpuTime1 = endTime1 - startTime1  
print(cpuTime1)

startTime2 = time.process_time()  
result2 = my_ifibo(10)             
endTime2 = time.process_time()   
cpuTime2 = endTime2 - startTime2  
print(cpuTime2)

