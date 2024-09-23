# Grade code
def calculateGrade(grade):
    if grade > 10 or grade < 0:
        return "Impossible"
    elif grade >= 9:
        return "A"
    elif grade == 8:
        return "B"
    elif grade == 7:
        return "C"
    elif grade == 6:
        return "D"
    else:
        return "F"

print(calculateGrade(10))