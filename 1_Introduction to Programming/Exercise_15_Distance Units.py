INCHES = 12
YARDS = 3 #Divide By 3
MILES = 5280 #Divde By 5280

ft = int(input("Enter Your Value in Feet(ft): "))

ftToInches = ft * INCHES
ftToYards = ft // YARDS
ftToMiles = format(ft / MILES, ".5f")

print(f'Feet to Inches: {ft} ft = {ftToInches} Inch(es), \nFeet to Yards: {ft} ft = {ftToYards} yd(s) \nand Feet to Miles: {ft} ft = {ftToMiles} Mile(s).')