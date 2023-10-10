# Author: Zhuo Xi Hong

# Import datetime to Indicate Current Date Instead of Manual Inputs
from datetime import datetime, date

month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

print("Welcome to The Alberta Voter Program!!")

cc = input("Are you a Canadian Citizen? ")
ar = input("Are you a Resident of Alberta? ")
dofbMon = int(input("What is the Month of Your Birthdate? (ie, May = 5) "))
dofbDay = int(input("What is the Day of Your Birthdate? "))
dofbYear = int(input("What is the Year of Your Birthdate? (ie, 1954) "))

#Date Values for Elif to Check If Date in Future
#currentDate = datetime.now().date()
#dofbDate = date(dofbYear, dofbMon, dofbDay)

if cc != 'yes' and cc != 'no':
    
    print("Invalid response to citizenship.")
    
elif ar != 'yes' and ar != 'no':
    
    print("Invalid response to residency.")
    
elif dofbMon < 1 or dofbMon > 12:
    
    print("Invalid month.")
    
elif dofbDay < 1 or dofbDay > 31:
    
    print("Invalid day.")
    
elif dofbYear < 1900 or dofbYear > year:
    
    print("Invalid year.")
    
else:
    
    ageYear = year - dofbYear

    # Check if the Birthday has Occurred This Year
    if month < dofbMon or (month == dofbMon and day < dofbDay):
        ageYear -= 1
    
    if ageYear < 18:
        
        print("You are not eligible to vote.")
    
    #This Elif Causing Problems
    #Febuary Leap Year Check        
    elif dofbMon == 2: 
    
        if (((dofbYear % 4) and (dofbYear % 100)) != 0):

            print("Invalid birth date.")

        elif (dofbYear % 400) == 0: 
    
            print("You are eligible to vote.")

    #Months Check to See 30 or 31 Days
    elif ((dofbMon == 4 or dofbMon == 6 or dofbMon == 9 or dofbMon == 11) and (dofbDay < 1 or dofbDay > 30)) or (dofbDay < 1 or dofbDay > 31): 
                                                                  
        print("Invalid birth date.")

    #Check if the Date is in the Future
    #elif currentDate > dofbDate: 
    
        #print("Invalid birth date.")
        
    elif cc == 'no':
        
        print("You are not eligible to vote.")
        
    elif ar == 'no':
        
        print("You are not eligible to vote.")
        
    else:
        
        print("You are eligible to vote.")
        
        
"""Problem Output: 
Test case 1:
Checking the last 29 characters in output:
===Your output:     "You are not eligible to vote."
===Expected output: "You are not eligible to vote."
===You are correct.

Test case 2:
Checking the last 25 characters in output:
===Your output:     "You are eligible to vote."
===Expected output: "You are eligible to vote."
===You are correct.

Test case 3:
Checking the last 32 characters in output:
===Your output:     "Invalid response to citizenship."
===Expected output: "Invalid response to citizenship."
===You are correct.

Test case 4:
Checking the last 14 characters in output:
===Your output:     "Invalid month."
===Expected output: "Invalid month."
===You are correct.

Test case 5:
Checking the last 19 characters in output:
===Your output:     "t eligible to vote."
===Expected output: "Invalid birth date."
===You are NOT correct.

Test case 6:
Checking the last 30 characters in output:
===Your output:     "Invalid response to residency."
===Expected output: "Invalid response to residency."
===You are correct.

Test case 7:
Checking the last 19 characters in output:
===Your output:     "t eligible to vote."
===Expected output: "Invalid birth date."
===You are NOT correct.

Test case 8:
Checking the last 19 characters in output:
===Your output:     "rthdate? (ie, 1954)"
===Expected output: "Invalid birth date."
===You are NOT correct.

Test case 9:
Checking the last 25 characters in output:
===Your output:     "You are eligible to vote."
===Expected output: "You are eligible to vote."
===You are correct.

Test case 10:
Checking the last 25 characters in output:
===Your output:     "You are eligible to vote."
===Expected output: "You are eligible to vote."
===You are correct.

Test case 11:
Checking the last 29 characters in output:
===Your output:     "You are not eligible to vote."
===Expected output: "You are not eligible to vote."
===You are correct.

Test case 12:
Checking the last 12 characters in output:
===Your output:     "Invalid day."
===Expected output: "Invalid day."
===You are correct.

Total correct: 9
Total errors: 0
** Total failed test cases: 3
"""