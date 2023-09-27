"""Author: Zhuo Xi Hong 
   Last Modified: Sept/26/2023

Prompt: Write a program that checks the eligibility to vote in Alberta elections.

Sources: 

    TA in Tutorial(s): 
    
        Debugging and Comment Convention. 
        
    String Block Comments: https://www.w3schools.com/python/python_comments.asp
    Try, Except ValueError: https://www.w3schools.com/python/python_try_except.asp

Line 18-22 Given in Assignment Files"""

# Import datetime to Indicate Current Date Instead of Manual Inputs
from datetime import datetime

month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

# Prompt Users for Values, Canadian Citizen (cc), Alberta Resident(ar) and Date of Birth(dofbMon, dofbDay, dofbYear)
cc = str(input("Are you a Canadian Citizen? "))
ar = str(input("Are you a Resident of Alberta? "))
dofbMon = int(input("What is the Month of Your Birthdate? (ie, May = 5) "))
dofbDay = int(input("What is the Day of Your Birthdate? "))
dofbYear = int(input("What is the Year of Your Birthdate? (ie, 1954) "))

# Conditional Determining If User Input is not 'yes' and 'no
if cc != 'yes' and cc != 'no': 
    
    # Try Case Determining if User Input is matches type 'str'
    try: 
        
        cc = cc
        
    except ValueError:
        
        print("Invalid response to citizenship.")
    
    print("Invalid response to citizenship.")

# Conditional Determining If User Input is not 'yes' and 'no
elif ar != 'yes' and ar != 'no':
    
    # Try Case Determining if User Input is matches type 'str'
    try: 
        
        ar = ar
        
    except ValueError:
        
        print("Invalid response to residency.")
    
    print("Invalid response to residency.")

# Conditional Determining if Month is in Month 1 to Month 12
elif dofbMon < 1 or dofbMon > 12:
    
    print("Invalid month.")
 
# Conditional Determining if Day is in Day 1 to Day 31
elif dofbDay < 1 or dofbDay > 31: 
        
    print("Invalid day.")

# Conditional Determining if Year is in 1900 to 2023
elif dofbYear < 1900 or dofbYear > 2023:
    
    print("Invalid year.")

# Conditional Determining if Year is in the Future
elif (dofbYear > year):
        
    print("Invalid year.")
        
# Conditional Determining if Leap Year Check, except 1900 Not Divisible by 4. 
elif dofbMon == 2 and dofbDay == 29 and dofbYear == 1900: 
    
    print("Invalid birth date.")

# Conditional Determining if Leap Year Check Other Than 1900. 
elif (dofbMon == 2 and dofbDay == 29) and (dofbYear % 4 != 0): 
        
    print("Invalid birth date.")
        
# Conditional Determining if 30 Day Check exceeds months 4, 6, 9, 11.
elif (dofbMon == 4 or dofbMon == 6 or dofbMon == 9 or dofbMon == 11) and (dofbDay > 30): 

    print("Invalid birth date.") 
    
# Conditionals Determining if Date in Future Check, 5 Conditional to Present Nicely and Include All Cases to Remove Flaws.  

    # Determines If Year, Month and Day is Greater Than Current Date.
elif ((dofbYear > year) and (dofbMon > month) and (dofbDay > day)):
    
    print("Invalid birth date.")

    # Determines If Year is Greater Than Current Date, when the Month and Day is the Same.
elif ((dofbYear > year) and (dofbMon == month) and (dofbDay == day)):
        
    print("Invalid birth date.")
    
    # Determines If Month is Greater Than Current Date, when the Year and Day is the Same.
elif ((dofbYear == year) and (dofbMon > month) and (dofbDay == day)):
        
    print("Invalid birth date.")
    
    # Determines If Day is Greater Than Current Date, when the Month and Year is the Same.
elif ((dofbYear == year) and (dofbMon == month) and (dofbDay > day)):
        
    print("Invalid birth date.")
    
    # Lastly Determines If Month and Day is Greater Than Current Date, when Year is the Same. 
elif ((dofbYear == year) and (dofbMon > month) and (dofbDay > day)):
        
    print("Invalid birth date.")
    
# Conditional That Checks If or If no the User is Eligible to Vote, If Passes All the Conditionals Above.
else: 
    
    # Determines ageYear to Find Age of User.
    ageYear = year - dofbYear
    
    # Conditional Determines If the Birthdate has Occured This Year
    if month < dofbMon or (month == dofbMon and day < dofbDay):
    
        ageYear -= 1
    
    # Conditional Determines If User is Under 18
    if ageYear < 18: 
    
        print("You are not eligible to vote.")
    
    # Conditional Determines If User has entered 'no' to Canadian Citizen and/or Alberta Resident.
    elif cc == 'no' or ar == 'no': 
    
        print("You are not eligible to vote.")
    
    # Conditional Determines if User is Older Than 18, is Canadian Citizen and Alberta Resident.
    elif (ageYear >= 18) and (cc == 'yes') and (ar == 'yes'): 
    
        print("You are eligible to vote.")