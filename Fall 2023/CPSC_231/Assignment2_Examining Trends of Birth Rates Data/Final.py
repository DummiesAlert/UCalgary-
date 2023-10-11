dataPt = int(input("How Many Data Points? "))
dataPoints = []
yearPts = []
birthRate = []

if dataPt <= 0: 
    
    print("Must enter at least one data point.")
    
else: 
    
    for i in range(dataPt):
    
        prevYear = 0
        
        year = int(input(f"What is the year of data point {i+1}? "))
        birthRate = float(input(f"What is the birth rate of data point {i+1}? "))
        
        if year < prevYear: 
            
            print("Years must be entered in order.")
            
        if year in yearPts: 
            
            print("Same year entered twice")
        
        if year <= 0:
            
            print("Invalid year.")
        else: 
            break
        
        if birthRate < 0.0: 
            
            print("Invalid birth rate.")
        
        prevYear = year

        #birthRate = format(birthRate, ".2f")
        year.append((yearPts))
        birthRate.append((birthRate))
        
        i -= 1
        
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


"""