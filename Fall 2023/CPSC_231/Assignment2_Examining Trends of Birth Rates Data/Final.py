"""Author: Zhuo Xi Hong 
   UCID: 30213715
   Last Modified: Oct/16/2023

Prompt: Write a program that Examines the Trends of Birth Rates with Data

Sources: 
    


"""

Years = [] 
birthRates = []

dataPoints = int(input("How many data points do you have? "))

inputYears = 0 
infoPassed = True
infoFailed = True

if dataPoints <= 0: 
    
    print("Must enter at least one data point.")

for i in range(dataPoints): 
    
    if infoFailed: 
        
        prevYear = inputYears
        i = str(i + 1)
        
        inputYears = int(input(f"What is the year of data point {i}?"))
        
        if inputYears in Years: 
            
            print("Same year entered twice.")
            infoFailed = False
            
        else: 
            
            if inputYears <= 0: 
                
                print("Invalid year.")
                infoFailed = False
                
            else: 
                
                if prevYear > inputYears:
                    
                    print("Years must be entered in order. ")
                    infoFailed = False
                    
                else: 
                    
                    Years.append(inputYears)
                    
                    inputRates = float(input(f"What is the birth rate of data point {i}?"))
                    
                    if inputRates < 0.0:
                        
                        print("Invalid birth rate.")
                        infoFailed = False
                        
                    else: 
                        
                        birthRates.append(inputRates)
                        infoPassed = False
                        
if infoFailed and not infoPassed:
    
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
            
            startIndex = birthRates[Years.index(startYear)]
            endIndex = birthRates[Years.index(endYear)]
            
            averRate = (startIndex + endIndex) / 2

            averRate = format(averRate, ".2f")
            print(f"The average birth rate of these two years is {averRate}.")

            if startIndex < endIndex:
                
                print("There is an upward trend.")
            
            elif startIndex > endIndex:
                
                print("There is a downward trend.")
            
            elif startIndex == endIndex:
                
                print("There is a sideways trend.")
                
"""
    
Bin: 

The following results are created by the auto-grader.

Test case 1:
Checking the last 35 characters in output:
===Your output:     "Must enter at least one data point."
===Expected output: "Must enter at least one data point."
===You are correct.

Test case 2:
Checking the last 13 characters in output:
===Your output:     "Invalid year."
===Expected output: "Invalid year."
===You are correct.

Test case 3:
Checking the last 31 characters in output:
===Your output:     "Years must be entered in order."
===Expected output: "Years must be entered in order."
===You are correct.

Test case 4:
Checking the last 24 characters in output:
===Your output:     "Same year entered twice."
===Expected output: "Same year entered twice."
===You are correct.

Test case 5:
Checking the last 19 characters in output:
===Your output:     "Invalid birth rate."
===Expected output: "Invalid birth rate."
===You are correct.

Test case 6:
Checking the last 30 characters in output:
===Your output:     "The start year does not exist."
===Expected output: "The start year does not exist."
===You are correct.

Test case 7:
Checking the last 28 characters in output:
===Your output:     "The end year does not exist."
===Expected output: "The end year does not exist."
===You are correct.

Test case 8:
Checking the last 77 characters in output:
===Your output:     "The average birth rate of these two years is 2.77.
There is a downward trend."
===Expected output: "The average birth rate of these two years is 2.77.
There is a downward trend."
===You are correct.

Test cases 9 to 12 are withheld until TA grades your assignment.
You should learn to test your code in scenarios that have not appeared above.

Total correct: 8
Total errors: 0
** Total failed test cases: 0
    
"""