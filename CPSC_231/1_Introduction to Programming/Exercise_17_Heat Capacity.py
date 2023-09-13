#PART 1
C = 4.186 #J/(g*C)

waterMass = float(input("Enter the Mass of Water Produced in Gram(s)/g: "))
chgTemp = float(input("Enter the Change in Temperature in Degrees *C: "))

q = C * waterMass * chgTemp

print("The Total Amount of Energy That Must Be Added or Removed to Achieve the Desired Temperature Change is:", q, "Joules (J)")

#PART 2

ELECCOST = 8.90 ("Cents")

kwh = q / (3.6 * (10 ** 6))