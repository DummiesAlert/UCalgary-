Years = []
Rates = []

dataPoints = int(input("How many data points do you have?"))

inputYears = 0 
infoGathered = False
stopRunning = False

if dataPoints <= 0:
    
    print("Must enter at least one data point.")
    
for counter in range(dataPoints): 
    
    if not stopRunning: 
        
        previousYear = inputYears
        
        inputYears = int(input("What is the year of data point " + str(counter + 1) + "?"))
        
        if inputYears in Years:
            
            print("Same year entered twice.")
            stopRunning = True
            
        else: 
            
            if inputYears <= 0: 
                
                print("Invalid year.")
                stopRunning = True
                
            else: 
                
                if previousYear > inputYears: 
                    
                    print("Years must be entered in order. ")
                    stopRunning = True
                
                else: 
                    
                    Years.append(inputYears)
                    
                    inputRates = float(input("What is the birth rate of data point " + str(counter + 1) + "?"))
                    
                    if inputRates < 0.0: 
                        
                        print("Invalid birth rate.")
                        stopRunning = True
                    
                    else: 
                        
                        Rates.append(inputRates)
                        
                        infoGathered = True
                        
if infoGathered and not stopRunning: 
    
    startYear = int(input("Which year would you like to start with?"))
    
    if startYear not in Years: 
        
        print("The start year does not exist.")
        
    else: 
        
        endYear = int(input("Which year would you like to end with?"))
        
        if endYear not in Years:
            
            print("The end year does not exist.")
            
        elif endYear < startYear: 
            
            print("End year must be after start year.")
            
        else: 
            
            averRate = (Rates[Years.index(startYear)] + Rates[Years.index(endYear)]) / 2

            averRate = format(averRate, ".2f")
            print(f"The average birth rate of these two years is {averRate}.")

            if Rates[Years.index(startYear)] < Rates[Years.index(endYear)]:
                
                print("There is an upward trend.")
            
            elif Rates[Years.index(startYear)] > Rates[Years.index(endYear)]:
                
                print("There is a downward trend.")
            
            elif Rates[Years.index(startYear)] == Rates[Years.index(endYear)]:
                
                print("There is a sideways trend.")