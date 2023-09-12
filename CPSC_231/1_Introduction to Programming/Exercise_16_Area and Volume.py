import math

pi = format(math.pi), ".2f"

rad = int(input("Enter the Radius: "))

areaCircle = pi * (rad ** 2)
areaVolume = (4/3)(pi * (rad ** 3))

print(f'The Area of a Circle is: {areaCircle} \nand the Volume of a Circle is: {areaVolume}')