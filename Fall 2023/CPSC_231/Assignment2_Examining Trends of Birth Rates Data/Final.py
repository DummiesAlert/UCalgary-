"""Author: Zhuo Xi Hong 
   UCID: 30213715
   Last Modified: Oct/17/2023

Prompt: Write a program that Examines the Trends of Birth Rates with Data

Sources: 

    List Nature with W3 Schools: 
    
        - Lists Comprehension: https://www.w3schools.com/python/python_lists_comprehension.asp
        - Lists with Loops: https://www.w3schools.com/python/python_lists_loop.asp
        - Adding/Appending to Lists:https://www.w3schools.com/python/python_lists_add.asp
        - Basic Lists: https://www.w3schools.com/python/python_lists.asp
        
    Tutorial: (Bool Logic)
    
        - TA Naman: Helped with Applying Bool Logic to Control the For Loop.

"""

#Creates List Boundaries
Years = [] 
birthRates = []

#Prompt User for Amount of Data Points:
dataPoints = int(input("How many data points do you have? "))

#Create Variables and Bool for Looping Control
inputYears = 0 
infoPassed = True
infoFailed = True

#Conditions Checking if dataPoints Less Than, Equal to 0
if dataPoints <= 0: 
    
    print("Must enter at least one data point.")
    
#For Loop Main Code
for i in range(dataPoints): 
    
    #Conditional Verifies dataPoint Again If Passed
    if infoPassed: 
        
        #For Loop, So Create Last Year as PrevYear to Restore New Year in Loop
        prevYear = inputYears
        
        #Create i as a String
        i = str(i + 1)
        
        #Prompt User for Year of dataPoint, when data point i
        inputYears = int(input(f"What is the year of data point {i}? "))
        
        #Checks if inputYear in List Years
        if inputYears in Years: 
            
            print("Same year entered twice.")
            infoPassed = False
        
        #If Passes Moves On
        else: 
            
            #Condition to Check if inputYears is Less Than 0
            if inputYears <= 0: 
                
                print("Invalid year.")
                infoPassed = False
            
            #If Passes Moves On
            else: 
                
                #Check if prevYear is Greater Than inputYears
                if prevYear > inputYears:
                    
                    print("Years must be entered in order. ")
                    infoPassed = False
                
                #If Passes Moves On
                else: 
                    
                    #Add inputYears to List Years
                    Years.append(inputYears)
                    
                    #Prompt User for birth rate i 
                    inputRates = float(input(f"What is the birth rate of data point {i}? "))
                    
                    #Check if inputRates if Greater Than 0.0 (float)
                    if inputRates < 0.0:
                        
                        print("Invalid birth rate.")
                        infoPassed = False
                    
                    #If Passes Moves On
                    else: 
                        
                        #Add inputRates to List birthRates
                        birthRates.append(inputRates)
                        infoFailed = False

#Double Checks If All Data has Passed, infoFailed = True and infoPassed = True.             
if infoPassed and not infoFailed:
    
    #Prompt for startYear from Years List in Order
    startYear = int(input("Which year would you like to start with? "))

    #Checks if startYear is in Years, if Not DNE
    if startYear not in Years: 
        
        print("The start year does not exist.")
        
    #If Passes Moves On
    else: 
        
        #Checks if endYear From Years List in Order
        endYear = int(input("Which year would you like to end with? "))
        
        #Checks if endYear is in Years, if not DNE
        if endYear not in Years: 
            
            print("The end year does not exist.")

        #Checks if endYear is Less Than startYear or if dataPoint == 1 and 
        elif (endYear < startYear) or (infoFailed and dataPoints == 1): 
            
            print("End year must be after start year.")
        
        #If Passes Moves On
        else: 
            
            #Locates Indexes of startyear and endYears to Match Data in List
            startIndex = birthRates[Years.index(startYear)]
            endIndex = birthRates[Years.index(endYear)]
            
            #Calculates Average Rate
            averRate = (startIndex + endIndex) / 2

            #Set averRate to 2 Decimal Points and print. 
            averRate = round(averRate, ".2f") #Changed to format
            print(f"The average birth rate of these two years is {averRate}.")

            #Conditional to Determine Upwards, Downwards and Sideways Trends. 
            if startIndex < endIndex:
                
                print("There is an upward trend.")
            
            elif startIndex > endIndex:
                
                print("There is a downward trend.")
            
            elif startIndex == endIndex:
                
                print("There is a sideways trend.")
                
[1,2]
[3,4]
                
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