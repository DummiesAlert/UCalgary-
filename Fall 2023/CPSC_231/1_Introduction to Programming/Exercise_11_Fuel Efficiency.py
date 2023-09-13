MPG_TO_LPER100KM = 235.21

mpg = float(input("Enter the Fuel Efficiency in Amercian Units of MPG (Miles Per Gallon): "))

con = mpg * MPG_TO_LPER100KM

print("The Equivalent Fuel Efficiency in Canadian Units of L/100Km is:", con)