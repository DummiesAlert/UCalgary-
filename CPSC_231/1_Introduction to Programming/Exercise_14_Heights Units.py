#Worked Solution

print("Enter Your Height:")

ft = int(input("Enter the Number of Feet: "))
inch = int(input("Enter the Number of Inches: "))

fInch = ft * 12 
fCent = fInch * 2.54

iInch = inch * 2.54

total = fCent + iInch

print(f'Feet to Inches To Centimeters: {ft} ft = {fInch} inch(es) = {fCent} cm \nInch(es) to Centimeters: {inch} inch(es) = {iInch} cm, and the Total Height is: {total} cm')

#Solution:
print("Enter Your Height:")

ft = int(input("Enter the Number of Feet: "))
inch = int(input("Enter the Number of Inches: "))

cm = (ft * 12 + inch) * 2.54

print("Your Height in CM is:", cm)