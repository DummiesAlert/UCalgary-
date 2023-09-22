from datetime import datetime

month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

print("Welcome to The Alberta Voter Program!!")

cc = str(input("Are you a Canadian Citizen? "))
ar = str(input("Are you a Resident of Alberta? "))
dofbMon = int(input("What is the Month of Your Birthdate? (ie, May = 5) "))
dofbDay = int(input("What is the Day of Your Birthdate? "))
dofbYear = int(input("What is the Year of Your Birthdate? (ie, 1954) "))

    
    if cc != 'yes' and cc != 'no': 
    
        print("Invalid response to citizenship.")
    
    elif ar != "yes" and ar != "no":
    
        print("Invalid response to residency.")
    
    try: 
        elif dofbMon < 1 or dofbMon > 12:
    
        print("Invalid month.")
 
#Value Other Than 31 Days
    elif dofbDay < 1 or dofbDay > 31: 
        
        print("Invalid day.")
    
#30 Day Check
    elif (dofbMon == 4 or dofbMon == 6 or dofbMon == 9 or dofbMon == 11) and (dofbDay < 1 or dofbDay > 30): 

        print("Invalid birth date.")
    
#Date in Future Check
    elif ((dofbYear > year) and (dofbMon > month) and (dofbDay > day)):
    
        print("Invalid birth date.")
    
    elif ((dofbYear > year) and (dofbMon == month) and (dofbDay == day)):
        
        print("Invalid birth date.")
    
    elif ((dofbYear == year) and (dofbMon > month) and (dofbDay == day)):
        
        print("Invalid birth date.")
    
    elif ((dofbYear == year) and (dofbMon == month) and (dofbDay > day)):
        
        print("Invalid birth date.")
    
    elif (dofbYear < year):
        
        print("Invalid year.")
        
#Leap Year Check
    elif (dofbYear % 4 != 0 and dofbYear % 100 == 0) or (dofbYear % 400 != 0):
        
        print("Invalid birth date.")
    
    elif dofbYear > 1900 or dofbYear < 2023:
    
        print("Invalid year.")
        
    else: 
    
        ageYear = year - dofbYear
    
        if month < dofbMon or (month == dofbMon and day < dofbDay):
    
            ageYear -= 1
        
        if ageYear < 18: 
    
            print("You are not eligible to vote.")
    
        elif cc == 'No' or ar == 'No': 
    
            print("You are not eligible to vote.")
    
        elif (ageYear >= 18) and (cc == 'yes') and (ar == 'yes'): 
    
            print("You are eligible to vote.")
            
