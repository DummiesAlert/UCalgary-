dataPt = int(input("How Many Data Points? "))

end = True
year = []
years = []
birthRates = []

i = 0
e = 0

if dataPt <= 0: 
    
    print("Must enter at least one data point.")
    end = False

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
    
    #Used for Test 3 + 4 not working
    if (i > 0 and year in years) or (year == prevYear) and end == True:
            print("Same year entered twice.")
            end = False
    
    elif ((prevYear != -1 and year <= prevYear) or year in years) and end == True:
        
        print("Years must be entered in order.")
        end = False
        
    elif end == True:
                   
        prevYear = years[-1]
            
        birthRate = float(input(f"What is the birth rate of data point {i + 1}? "))
        birthRates.append(birthRate)
    
        if birthRate < 0.0 and end == True: 
        
            print("Invalid birth rate.")
            end = False
            
    prevYear = years[-1]
            
if end == 1: 
    
            startYear = int(input("Which year would you like to start with? "))

            if startYear not in years:
    
                print("The start year does not exist.")

            endYear = int(input("Which year would you like to end with? "))

            if endYear not in years:
    
                print("The end year does not exist.")
    
            if endYear <= startYear: 
    
                print("End year must be after start year.")
    
            #Not Detecting year in years
            startIndex = years.index(startYear)
            endIndex = years.index(endYear)
            
            a = birthRates[startIndex]
            b = birthRates[endIndex]
    
            averBirthRate = (a + b) / 2
            averBirthRate = round(averBirthRate, 2)

            if a < b: 
    
                trend = "There is an upward trend." 
    
            elif a > b: 
    
                trend = "There is a downward trend." 
    
            elif a == b: 
    
                trend = "There is a sideways trend." 
                
            else: 
                
                end == False
    
            #print(f"The average birth rate of these two years is: {averBirthRate:.2f}")
            print(f"The average birth rate of these two years is {averBirthRate:.2f}.")
            print(trend)
            
"""
      
Screen Dump: 

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
===Your output:     "ta point 2? Invalid birth rate."
===Expected output: "Years must be entered in order."
===You are NOT correct.

Test case 4:
Checking the last 24 characters in output:
===Your output:     "t 2? Invalid birth rate."
===Expected output: "Same year entered twice."
===You are NOT correct.

Test case 5:
Checking the last 19 characters in output:
===Your output:     "Invalid birth rate."
===Expected output: "Invalid birth rate."
===You are correct.

Test case 6:
Error: Traceback (most recent call last):
  File "/home/profs/richard.zhao1/231/test/testzhuoxi.h.py", line 74, in <module>
    startIndex = years.index(startYear)
                 ^^^^^^^^^^^^^^^^^^^^^^
ValueError: 1903 is not in list


Test case 7:
Error: Traceback (most recent call last):
  File "/home/profs/richard.zhao1/231/test/testzhuoxi.h.py", line 75, in <module>
    endIndex = years.index(endYear)
               ^^^^^^^^^^^^^^^^^^^^
ValueError: 1904 is not in list


Test case 8:
Checking the last 77 characters in output:
===Your output:     "The average birth rate of these two years is 2.77
There is a downward trend."
===Expected output: "The average birth rate of these two years is 2.77.
There is a downward trend."
===You are NOT correct.

Test cases 9 to 12 are withheld until TA grades your assignment.
You should learn to test your code in scenarios that have not appeared above.

"""