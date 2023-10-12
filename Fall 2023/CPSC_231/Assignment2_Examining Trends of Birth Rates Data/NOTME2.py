dataPt = int(input("How Many Data Points? "))
yearPts = []
birthRates = []

if dataPt <= 0: 
    print("Must enter at least one data point.")
else: 
    prevYear = 0
    for i in range(dataPt):
        
        year = int(input("What is the year of data point? "))
        birthRate = float(input("What is the birth rate of data point? "))
        
        if year < prevYear: 
            print("Years must be entered in order.")
        elif year in yearPts: 
            print("Same year entered twice")
        elif year <= 0:
            print("Invalid year.")
        elif birthRate < 0.0: 
            print("Invalid birth rate.")
        else:
            prevYear = year
            yearPts.append(year)
            birthRates.append(birthRate)

# Data Analysis
startYear = int(input("Enter the start year: "))
if startYear not in yearPts:
    print("The start year does not exist.")
else:
    endYear = int(input("Enter the end year: "))
    if endYear not in yearPts:
        print("The end year does not exist.")
    elif endYear <= startYear:
        print("End year must be after start year.")
    else:
        startIndex = yearPts.index(startYear)
        endIndex = yearPts.index(endYear)
        avgBirthRate = sum(birthRates[startIndex:endIndex+1]) / (endIndex - startIndex + 1)
        print(f"The average birth rate from {startYear} to {endYear} is {avgBirthRate}")
