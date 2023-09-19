# Author: Zhuo Xi Hong

# Import datetime to Indicate Current Date Instead of Manual Inputs
from datetime import datetime
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
    
elif dofbMon < 1 or dofbMon > 12:
    
    print("Invalid month.")
    
elif dofbDay < 1 or dofbDay > 31: #or (dofbMon == [1, 3, 5, 7, 8, 10, 12] and dofbDay == 31) or (dofbMon == [2] and dofbDay >= 29):
    
    print("Invalid day.")
    
elif dofbYear < 1900 or dofbYear > 2023:
    
    print("Invalid year.")
    
else:
    
    ageYear = year - dofbYear
    ageMonth = month - dofbMon
    ageDay = day - dofbDay
    
    if ageYear < 18 or ageMonth <= 2 or ageDay <= 3:
        
        print("Invalid birth date.")
        print("You are not eligible to vote.")
        
    elif cc == 'no':
        
        print("Not a Canadian Citizen.")
        print("You are not eligible to vote.")
        
    elif ar == 'no':
        
        print("Not an Alberta Resident.")
        print("You are not eligible to vote.")
        
    else:
        
        print("You are eligible to vote.")
        
        
"""Problem Output:

Test case 1:
Checking the last 29 characters in output:
===Your output:     "1954) Not a Canadian Citizen."
===Expected output: "You are not eligible to vote."
===You are NOT correct.

Test case 2:
Checking the last 25 characters in output:
===Your output:     "You are eligible to vote."
===Expected output: "You are eligible to vote."
===You are correct.

Test case 3:
Checking the last 32 characters in output:
===Your output:     " Invalid response to citizenship"
===Expected output: "Invalid response to citizenship."
===You are NOT correct.

Test case 4:
Checking the last 14 characters in output:
===Your output:     "Invalid month."
===Expected output: "Invalid month."
===You are correct.

Test case 5:
Checking the last 19 characters in output:
===Your output:     "Invalid birth date."
===Expected output: "Invalid birth date."
===You are correct.

Test case 6:
Checking the last 30 characters in output:
===Your output:     "Invalid response to residency."
===Expected output: "Invalid response to residency."
===You are correct.

Test case 7:
Checking the last 19 characters in output:
===Your output:     "Invalid birth date."
===Expected output: "Invalid birth date."
===You are correct.

Test case 8:
Checking the last 19 characters in output:
===Your output:     "e eligible to vote."
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
===Your output:     "54) You are eligible to vote."
===Expected output: "You are not eligible to vote."
===You are NOT correct.

Test case 12:
Checking the last 12 characters in output:
===Your output:     "Invalid day."
===Expected output: "Invalid day."
===You are correct.

Total correct: 8
Total errors: 0
** Total failed test cases: 4"""