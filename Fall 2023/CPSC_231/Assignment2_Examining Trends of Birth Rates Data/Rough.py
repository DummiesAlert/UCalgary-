dataPoints = int(input("How Many Data Points?"))

i = 1
data = []

while i <= dataPoints:
    year = int(input(f"What is the year of data point {i}? "))
    birth_rate = float(input(f"What is the birth rate of data point {i}? "))

    if 0 <= birth_rate <= 2:
        data.append((year, birth_rate))
        i += 1
    else:
        print("Invalid birth rate. Please enter a value between 0 and 2.")

print("Data entered successfully:")
for year, rate in data:
    print(f"Year: {year}, Birth Rate: {rate:.2f}")
