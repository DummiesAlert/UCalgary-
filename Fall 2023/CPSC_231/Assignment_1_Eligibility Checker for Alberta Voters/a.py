from datetime import datetime
month = datetime.now().month
day = datetime.now().day
year = datetime.now().year

def quit():
    
    print("You DO NOT MEET the Basic Requirements.")
    
print("Welcome to The  Alberta Voter Program!!")

cc = str(input("Are you a Canadian Citizen? "))
    
ar = str(input("Are you a Resident of Alberta? "))

dofbMon = int(input("What is the Month of Your Birthdate? (ie, May = 5) "))

dofbDay = int(input("What is the Day of Your Birthdate? "))

dofbYear = int(input("What is the Year of Your Birthdate? (ie, 1954) "))

if cc != 'Yes' or 'No':
    
    quit()
    print("Invalid Response to Citizenship")
    
if ar != 'Yes' or 'No':
    
    quit()
    print("Invalid Response to Residency")
    
if dofbMon != (1-12): 
    
    quit()
    print("Invalid Month")
    
if dofbDay != (1-31): 
    
    quit()
    print("Invalid Day")

if dofbYear != (1900-2023):
        
    quit()
    print("Invalid Year")
    
age = 2023 - dofbYear

if age < 18:
    
    quit()
    print("Minor, Under 18")
    
else: 
    
    print("You are Eligible to Vote")
    
if cc == 'No':
    
    quit()
    print("Not a Canadian Citizen")
    
elif ar == 'No':
    
    quit()
    print("Not a Alberta Resident")
    
else: 
    
    print("You are Eligible to Vote")