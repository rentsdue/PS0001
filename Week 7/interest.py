# 2. If a certain amount of money (called the principal P) is invested in a bank account, earning an interest
# rate i compounded annually, the total amount of money Tn that will be in the account after n years
# is given by:
# Tn = P ∗ (1 + i) ^ n
# Write a function that will receive input arguments for P, i, and n, and will return the total amount of
# money Tn.
# Also, give an example of calling the function, printing in a sentence the inputs and the output of the
# function. For that, try two methods to use the function: write the function directly in your script, or
# write the function in a separate file that you will import beforehand.

def totalMoney(principal, interest, years):
    return principal * (1 + interest / 100) ** years

print(totalMoney(100, 5, 3))