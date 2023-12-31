"""
    
Sources: 

    Lists: https://www.w3schools.com/python/ref_list_append.asp
    
"""

dataPt = int(input("How Many Data Points? "))

if dataPt <= 0: 
    
    print("Must enter at least one data point.")

years = []
birthRates = []
prevYear = -1

for i in range(0, dataPt, 1):
    
    year = int(input(f"What is the year of data point {i + 1}? "))
    
    if year < 0: 
        
        print("Invalid year.")
    
    elif year in years: 
        
        print("Same year entered twice.")
    
    elif prevYear != -1 and year <= prevYear:
        
        print("Years must be entered in order.")
    
    birthRate = float(input(f"What is the birth rate of data point {i + 1}? "))
    
    if birthRate < 0.0: 
        
        print("Invalid birth rate.")
    
    years.append(year)
    birthRates.append(birthRate)
    prevYear = years[-1]
    
    dataPt = 0

while dataPt != 0: 
    
    startYear = int(input("Which year would you like to start with? "))

    if startYear not in years:
    
        print("The start year does not exist.")

    endYear = int(input("Which year would you like to end with? "))

    if endYear not in years:
    
        print("The end year does not exist.")
    
    if endYear <= startYear: 
    
        print("End year must be after start year.")
    
    #if startyear[] = years[1] then a = birthrate[1]
    
    # then (a x b) /2 = average. 
    averBirthRate = (years[startYear] == years[endYear]) / 2
    averBirthRate = round(averBirthRate, 2)

    if years[startYear] < years[endYear]: 
    
        trend = "There is an upward trend." 
    
    elif years[startYear] > years[endYear]: 
    
        trend = "There is a downward trend." 
    
    elif years[startYear] == years[endYear]: 
    
        trend = "There is a sideways trend." 
    
    #print(f"The average birth rate of these two years is: {averBirthRate:.2f}")
    print(f"The average birth rate of these two years is: {averBirthRate:.2f}")
    print(trend)