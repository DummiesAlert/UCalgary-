def input_data_points():
    while True:
        dataPt = int(input("How Many Data Points? "))
        if dataPt > 0:
            return dataPt
        print("Must enter at least one data point.")

def input_year_and_birth_rate(i, years):
    while True:
        year = int(input(f"What is the year of data point {i + 1}? "))
        if year <= 0 or (years and year <= years[-1]):
            print("Invalid year or years not in order.")
            continue
        birthRate = float(input(f"What is the birth rate of data point {i + 1}? "))
        if birthRate < 0.0:
            print("Invalid birth rate.")
            continue
        return year, birthRate

dataPt = input_data_points()
years = []
birthRates = []

for i in range(dataPt):
    year, birthRate = input_year_and_birth_rate(i, years)
    years.append(year)
    birthRates.append(birthRate)

startYear = int(input("Which year would you like to start with? "))
endYear = int(input("Which year would you like to end with? "))

if startYear not in years or endYear not in years or endYear <= startYear:
    print("Invalid start or end year.")
else:
    start_index = years.index(startYear)
    end_index = years.index(endYear)
    averBirthRate = sum(birthRates[start_index:end_index+1]) / (end_index-start_index+1)
    averBirthRate = round(averBirthRate, 2)

    if birthRates[start_index] < birthRates[end_index]: 
        trend = "There is an upward trend." 
    elif birthRates[start_index] > birthRates[end_index]: 
        trend = "There is a downward trend." 
    else: 
        trend = "There is a sideways trend." 

    print(f"The average birth rate of these two years is: {averBirthRate:.2f}")
    print(trend)