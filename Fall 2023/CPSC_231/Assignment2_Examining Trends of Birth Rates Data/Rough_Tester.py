"""dataPts = int(input("How Many Data Points?"))
dataPoints = []

dataPts = format(dataPts, ".2f")


dataPts = 1
data = []

while dataPts == dataPts:
    
    year = int(input(f"What is the year of data point {dataPts}? "))
    birth_rate = float(input(f"What is the birth rate of data point {dataPts}? "))

    if birth_rate >= 0:
        data.append((year, birth_rate))
        dataPts += 1
    else:
        print("Invalid birth rate. Please enter a value between 0 and 2.")

print("Data entered successfully:")
for year, rate in data:
    print(f"Year: {year}, Birth Rate: {rate:.2f}")"""
    
"""dataPt = float(input("How Many Data Points? "))
dataPoints = []

dataPt = int(format(dataPt, ".0f"))
dataPts = format(dataPt, ".2f")

for i in range[dataPts]:
    
    year = int(input(f"What is the year of data point {i+1}? "))
    birth_rate = float(input(f"What is the birth rate of data point {i+1}? "))
    
    dataPoints.append((year, birth_rate))"""
    
# Create an empty dictionary to store the variables
years = {}

# Prompt the user for input
num_years = int(input("How many years do you want to enter? "))

# Use a for loop to collect user input and store it in the dictionary
for i in range(1, num_years + 1):
    user_input = input(f"Enter a value for year {i}: ")
    years[f'year{i}'] = user_input

# Access the stored variables
for year, value in years.items():
    print(f"{year}: {value}")
