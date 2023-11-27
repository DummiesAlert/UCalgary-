from math import sqrt

height = float(input("Enter a height in metres: "))
initialSpeed = 0
GRAVITY = 9.8 

finalVel = sqrt(2 * GRAVITY * height)
finalVel = format(finalVel, ".2f")

print(f"It will hit the ground at {finalVel} m/s")