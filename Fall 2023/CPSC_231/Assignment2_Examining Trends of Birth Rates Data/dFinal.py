dataPt = int(input("How Many Data Points? "))

end = True
year = []
years = []
birthRates = []

end = True
i = 0
e = 0

if dataPt <= 0: 
    
    print("Must enter at least one data point.")

for i in range(0, dataPt, 1):
    
    if i >= dataPt:
    
        end = 1
    
    prevYear = -1
        
    if end == True:
        
        year = int(input(f"What is the year of data point {i + 1}? "))
        years.append(year)

    if year <= 0 and end == True: 
        
        print("Invalid year.")
        end = False
    
    if (i > 0 and year in years) and (year == prevYear):
            print("Same year entered twice.")
            end = False
    
    elif (prevYear != -1 and year <= prevYear) and end == True:
        
        print("Years must be entered in order.")
        end = False
        
    elif end == True:           
        prevYear = years[-1]
            
        birthRate = float(input(f"What is the birth rate of data point {i + 1}? "))
        birthRates.append(birthRate)
    
        if birthRate < 0.0 and end == True: 
        
            print("Invalid birth rate.")
            end = False
            
if end == 1: 
    
            startYear = int(input("Which year would you like to start with? "))

            if startYear not in years:
    
                print("The start year does not exist.")

            endYear = int(input("Which year would you like to end with? "))

            if endYear not in years:
    
                print("The end year does not exist.")
    
            if endYear <= startYear: 
    
                print("End year must be after start year.")
        
            try:
    
                index = years.index(year)
                a = birthRates[index]
        
            except ValueError:
    
                print("")

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