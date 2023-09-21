# convert miles per gallon to liters/100km

miles_per_gallon = input("Enter miles per gallon: ")

# 1 mile = 1.609344 kilometers
km_per_gallon = 1.609344 * miles_per_gallon

# 1 US gallon = 3.78541178 litres
km_per_litre = 3.78541178 * km_per_gallon

# flip litre and km
litres_per_km = 1 / km_per_liter

# calculate per 100 km
litres_per_100km = litres_per_km * 100

# output result
print("in litres / 100 km: ", litres_per_100km)

    #Right
    
    # Conversion Str to Float
    # Line 3: Identify the Type Value
    # miles_per_gallon = float(input("Enter miles per gallon: "))

    # Logical Error
    # Line 8: Wrong Math
    # km_per_litre = km_per_gallon / 3.78541178

    # Runtime Error
    # Line 12: Litre Spelled Wrong 
    # litres_per_km = 1 / km_per_litre
    
    # Runtime Error/Logical Error
    # Line 12: Might be Divide by 0

    # Syntax Error
    # Line 18: the print outline is missing a comma to display the variable
    # print("in litres / 100 km: ", litres_per_100km)

# Line 18: Missing Output Formatting
# print("in litres / 100 km: ", format(litres_per_100km, ".2f"))