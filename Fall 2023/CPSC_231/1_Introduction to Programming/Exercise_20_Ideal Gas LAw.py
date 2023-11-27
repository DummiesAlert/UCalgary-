pressure = float(input("Enter the Pressure in Pascals: "))
volume = float(input("Enter the Volume in Litres: "))
temp = float(input("Enter the Temperature [Kelvins, Celsius or Fahrenheit]: "))
tempUnit = str(input("What is the Unit Temperature was Used [Kelvins (k), Celsius (c) or Fahrenheit (f)]: ")).lower()

GASCONSTANT = 8.314

if tempUnit == 'k':
    
    kelvin = temp
    
elif tempUnit == 'c':
    
    kelvin = temp + 273.15
    
elif tempUnit == 'f':
    
    kelvin = ((temp - 32) * (5 / 9)) + 273.15

moles = (pressure * volume) / (GASCONSTANT * kelvin)

print(f"The moles from the Ideal Gas Law is {moles} moles")

"""
Write a program that computes the amount of gas in moles when the user supplies
the 

pressure, 
volume and 
temperature. 

Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit.

Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
multiply it by 5/9 and then add 273.15 to it

"""