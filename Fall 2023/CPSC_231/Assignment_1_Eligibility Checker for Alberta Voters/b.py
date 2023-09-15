# Author: Zhuo Xi Hong

# Import datetime to Indicate Current Date Instead of Manual Inputs
from datetime import datetime
month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

def quit():

    print("You Are Not Eligible To Vote")

print("Welcome to The Alberta Voter Program!!")

cc = input("Are you a Canadian Citizen? ")

ar = input("Are you a Resident of Alberta? ")

dofbMon = int(input("What is the Month of Your Birthdate? (ie, May = 5) "))

dofbDay = int(input("What is the Day of Your Birthdate? "))

dofbYear = int(input("What is the Year of Your Birthdate? (ie, 1954) "))

if cc != 'Yes' and cc != 'No':
    
    quit("Invalid Response to Citizenship")
    
elif ar != 'Yes' and ar != 'No':
    
    quit("Invalid Response to Residency")
    
elif dofbMon < 1 or dofbMon > 12:
    
    quit("Invalid Month")
    
elif dofbDay < 1 or dofbDay > 31:
    
    quit("Invalid Day")
    
elif dofbYear < 1900 or dofbYear > 2023:
    
    quit("Invalid Year")
    
else:
    
    age = year - dofbYear
    
    if age < 18:
        
        quit("Minor, Under 18")
        
    elif cc == 'No':
        
        quit("Not a Canadian Citizen")
        
    elif ar == 'No':
        
        quit("Not an Alberta Resident")
        
    else:
        
        print("You are Eligible to Vote")