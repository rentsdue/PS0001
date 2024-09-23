# Imagine a user menu to order pizzas online. The user is first asked to choose between 3 different types
# of pizzas (margherita at S$15.5, marinara at S$17.5 and napoletana at S$18) and once the pizza type
# selected he is invited to type the amount of such pizzas he would like to order. Finally, the user is
# asked if he would like to stop the ordering. If not, then the menu comes back to asking to select the
# pizza. If yes, the final price is printed according to the pizzas ordered and the program stops.

exitBool = True
cost = 0
while exitBool:
    pizzaType = input("Choose between 3 types of pizzas: Margherita (M) at $15.5, marinara (A) at $17.5, and nopletana (N) at $18. ")
    pizzaNo = int(input("How many pizzas of that type would you want? "))
    pizzaBool = input("If you want to stop, type \"y\". Otherwise, type \"n\". ")
    if pizzaType == "M":
        cost += 15.5 * pizzaNo
    elif pizzaType == "A":
        cost += 17.5 * pizzaNo
    elif pizzaType == "N":
        cost += 18 * pizzaNo
    if pizzaBool == "y":
        print("The total cost of your order is: " , cost)
        exitBool = False