
# Write a script currency.py that will prompt the user for an amount in Singapore Dollars, and then
# to which foreign currency he would like to convert this amount (’E’ for Euros, ’U’ for US Dollars, ’J’
# for Japanese Yen). The script will then print the original amount and the converted amount. The
# output can look like this:

singaporeDollars = float(input("Enter the amount in Singapore Dollars: "))
convertTo = input("Do you want to convert this amount in Euros (E), US Dollars (U) or Japanese Yen (J)? ")

if convertTo == "U":
    print(singaporeDollars, " equals ", singaporeDollars * 0.70, "EUR.")
elif convertTo == "E":
    print(singaporeDollars, " equals ", singaporeDollars * 0.77, "USD.")
elif convertTo == "J":
    print(singaporeDollars, " equals ", singaporeDollars * 111.45, "USD.")
else:
    print("Please type in a valid letter next time.")
