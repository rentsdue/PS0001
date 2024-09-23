def quadraticFormula(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "No real roots!"
    elif discriminant == 0:
        return (-b / (2 * a))
    else:
        return ("The real roots of the equation are: " , ((-b / (2 * a)) + ((discriminant ** 0.5) / (2 * a))), " and ", ((-b / (2 * a)) - ((discriminant ** 0.5) / (2 * a))))

print(quadraticFormula(0.5, -3.5, 5))