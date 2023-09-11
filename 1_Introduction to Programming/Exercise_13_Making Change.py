#NEEDED HELP

CENTSTOONIE = 200
CENTSLOONIE = 100
CENTSQUARTER = 25
CENTSDIME = 10
CENTSNICKEL = 5

userGave = int(input("Enter the Amount in Cent(s): "))

print(" ", userGave // CENTSTOONIE, "Toonie(s)")
userGave = userGave % CENTSTOONIE

print(" ", userGave // CENTSLOONIE, "Loonie(s)")
userGave = userGave % CENTSLOONIE

print(" ", userGave // CENTSQUARTER, "Quarter(s)")
userGave = userGave % CENTSQUARTER

print(" ", userGave // CENTSDIME, "Dime(s)")
userGave = userGave % CENTSDIME

print(" ", userGave // CENTSQUARTER, "Quarter(s)")
userGave = userGave % CENTSQUARTER

print(" ", userGave, "Pennie(s)")