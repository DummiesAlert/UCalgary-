SQFT_PER_ACRE = 43560

length = float(input("Enter the Length (In Feet): "))
width = float(input("Enter the Width (In Feet): "))

Acres = (length * width) / SQFT_PER_ACRE

print("The Area of the Field is ", Acres, "In Acres. ")
