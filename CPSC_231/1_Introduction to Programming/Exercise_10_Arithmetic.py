import math 

a = int(input("Enter A Value as a: "))
b = int(input("Enter A Value as b: "))

sum = a + b
sub = b - a
pro = a * b
div = a / b
rem = a % b
log = math.log10(a)
squ = a ** b

print(f'Sum: {sum}, Difference: {sub}, Product: {pro}, Quotient: {div}, Remainder {rem}, Log10(a): {log}, a^b: {squ}')