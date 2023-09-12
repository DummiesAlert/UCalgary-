l = 0.10
m = 0.25

lessThan1 = float(input("Enter Amount of Bottles Less Than One Liter: "))
moreThan1 = float(input("Enter Amount of Bottles More Than One Liter: "))

less = lessThan1 * l
more = moreThan1 * m
total = format((less + more), ".2f")

print("Amount Being Returned: $", total)