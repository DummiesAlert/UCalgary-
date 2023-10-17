dataPt = int(input("How Many Data Points? "))
dataPoints = []
yearPts = []
birthRts = []

if dataPt <= 0: 
    
    print("Must enter at least one data point.")
    
else: 
    
    for i in range(dataPt):
    
        prevYear = 0
        
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
            birthRts.append(birthRate)
         
"""

Step 4:

Data analysis: Now that we have the data, we want to do some analysis on the data. Let’s 
calculate the average birth rate of two given years and calculate the trend. 
The next step in the code is to ask the user to enter the two years they want to use. Assume the 
entered years are integers.  
 
Add error checking in the following order: 
• If start year does not exist as an existing data point (as entered by user in step 2), no 
other code should run. The code should output the following message and stop: “The 
start year does not exist.”  Check this as soon as the user enters the start year. 
• If end year does not exist as an existing data point (as entered by user in step 2), no 
other code should run. The code should output the following message and stop: “The 
end year does not exist.” 
• The end year should be after the start year. If not, no other code should run, and your 
code should output “End year must be after start year.” and stop. 

Step 5: 

Based on the user entered years, the code will calculate and output the average birth rate of the 
two years (using only the data from these two years, not any years in between), shown to 2 
decimal places.  Round if longer (2.337 becomes 2.34); pad 0s if shorter (2 becomes 2.00). 
It will also output either “There is an upward trend.” , “There is a downward trend.” ,  or “There 
is a sideways trend.”  depending on whether the birth rate increased, decreased, or remained 
the same.
"""