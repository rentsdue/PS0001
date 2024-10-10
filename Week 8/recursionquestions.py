# 1. The sum 𝑓(𝑛) = 1 + 2 + 3 + … + 𝑛 can be defined as a recursive function:
# 𝑓(0) = 0 𝑖𝑓 𝑛 == 0
# 𝑓(𝑛) = 𝑛 + 𝑓(𝑛 – 1) 𝑖𝑓 𝑛 > 0
# Write a recursion function 𝑚𝑦_𝑎𝑑𝑑(𝑛) to calculate the sum of a number sequence. Test the function.

def my_add(n):
    if n == 0:
        return 0
    else:
        return n + my_add(n - 1)

print(my_add(5))

# 2. The factorial of a number 𝑛 is 𝑛! = 1 × 2 × 3 × … × 𝑛. The calculation is another example to use
# recursive function:
# 𝑓𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛) = 1 𝑖𝑓 𝑛 == 0
# 𝑓𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛) = 𝑛 × 𝑓𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛 – 1) 𝑖𝑓 𝑛 > 0
# Write a recursion function 𝑚𝑦_𝑓𝑎𝑐𝑡𝑜𝑟𝑖𝑎𝑙(𝑛) to calculate the result of 𝑛!. Test the function.

def my_factorial(n):
    if n == 0:
        return 1
    else:
        return n * my_factorial(n - 1)

print(my_factorial(6))

# 3. Another example to use recursive function is to find the greatest common divisor (gcd) of two integers a and
# b. The procedure is below:
# 𝐶𝑜𝑚𝑝𝑢𝑡𝑒 𝑟,𝑡ℎ𝑒 𝑚𝑜𝑑𝑢𝑙𝑢𝑠 𝑜𝑓 𝑎 𝑎𝑛𝑑 𝑏.
# 𝑟𝑒𝑡𝑢𝑟𝑛 𝑏 𝑖𝑓 𝑟 == 0
# 𝑟𝑒𝑡𝑢𝑟𝑛 1 𝑖𝑓 𝑟 == 1
# 𝑒𝑙𝑠𝑒 𝑟𝑒𝑝𝑒𝑎𝑡 𝑡ℎ𝑒 𝑎𝑏𝑜𝑣𝑒 𝑝𝑟𝑜𝑐𝑒𝑠𝑠 𝑓𝑜𝑟 𝑏 𝑎𝑛𝑑 r

def gcd(a, b): 
    r = a % b
    if r == 0:
        return b
    elif r == 1:
        return 1
    else:
        return gcd(b, r)

print(gcd(1000, 999))

def isPalindrome(str):
    if len(str) <= 1:
        return True
    elif str[0] == str[-1]:
        return isPalindrome(str[1:-1])
    else:
        return False

print(isPalindrome("bobob"))