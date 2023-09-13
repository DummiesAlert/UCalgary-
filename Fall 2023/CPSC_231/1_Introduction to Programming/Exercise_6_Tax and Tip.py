TAX = 0.05
TIP = 0.10

mealCost = float(input("Enter Cost of Meal: "))

tax = mealCost * TAX
tip = mealCost * TIP

total = format(mealCost + tax + tip, ".2f")

print("The Tax Will Be $" ,tax , "and The Tip Will Be $", tip, "Making The Total To Be $", total)