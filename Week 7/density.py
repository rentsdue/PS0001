#  Write a script Density.py that will compute the population density of a given country. The script
# will do the following:
#  prompt the user to input the the name of the country, the total area and the population
#  call a function countryDensity to compute the density. The function takes two inputs (the total
# area and the population) and returns the density
#  output the name of the country and the density in the format as shown below
# Note, the density should be a whole number.

def countryDensity(population, area):
    return int(population / area)

print("Computation of Density")
country = input("Enter the name of the country: ")
area = float(input("Enter the area (in km2): "))
population = float(input("Enter the population: "))

print("The population density of", country, "is", countryDensity(population, area), "people per km2")