# Write a script time diff.py that will compute the number of seconds contained in duration entered
# by the user. The script will do the following:
#  prompt the user to input a number of years, days and hours (you can assume that only integers
# will be entered by the user)
#  call a function convert to compute the number of seconds contained in that duration. The
# function takes three inputs (the number of years, days and hours) and returns the number of
# seconds. You can assume for simplicity that all years have 365 days.
#  output the number of seconds in the format as shown below

def noOfSeconds(y, d, h):
    return y * 31536000 + d * 86400 + h * 3600

years = int(input("Enter the number of years: "))
days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))

print("There are" , noOfSeconds(years, days, hours), "seconds in", years, "years," , days, "days,", "and", hours, "hours.")
