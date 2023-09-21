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

if cc != 'yes' and cc != 'no':
    
    print("Invalid response to citizenship.")
    
elif ar != 'yes' and ar != 'no':
    
    print("Invalid response to residency.")
    
elif dofbMon <= 1 or dofbMon >= 12:
    
    print("Invalid month.")
    
elif dofbDay <= 1 or dofbDay >= 31:
    
    print("Invalid day.")
    
elif dofbYear <= 1900 or dofbYear >= 2023:
    
    print("Invalid year.")
    
else:
    
    ageYear = year - dofbYear
    
    #Current Date to Date Of Birth Validation.
    currentDate = date.today()
    dofbDate = date(dofbYear, dofbMon, dofbDay)

    # Check if the Birthday has Occurred This Year
    if month < dofbMon or (month == dofbMon and day < dofbDay):
        ageYear -= 1 
    
    if currentDate > dofbDate: 

        print(currentDate)
        print(dofbDate)
        print("Invalid birth date.")

    #Months Check to See 30 or 31 Days, and Febuary Leap Year Check
    elif (((dofbYear % 4) and (dofbYear % 100)) != 0) or ((dofbMon == 4 or dofbMon == 6 or dofbMon == 9 or dofbMon == 11) and (dofbDay < 1 or dofbDay > 30)) or (dofbDay < 1 or dofbDay > 31): 
                                                                  
        print("Invalid birth date.")

    #Check if the Date is in the Future
    
    #Date Values for Elif to Check If Date in Future
    
    elif ageYear < 18:
        
        print("You are not eligible to vote.")

    elif cc == 'no':
        
        print("You are not eligible to vote.")
        
    elif ar == 'no':
        
        print("You are not eligible to vote.")
    
    #Febuary Leap Year Check
    elif (dofbYear % 400) == 0:
        
        print("You are eligible to vote.")
        
    else:
        
        print("You are eligible to vote.")
        
        
"""Problem Output: 

"""