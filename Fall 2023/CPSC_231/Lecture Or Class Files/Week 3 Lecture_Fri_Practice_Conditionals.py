age = int(input("How Old Are You?"))

if age >= 18: 
    
    print("You are Eligible to Vote")
    
elif age < 18: 
    
    ageDiff = 18 - age
    print("You can vote in", ageDiff, "Years.")
    
elif age >= 18 or age < 18: 
    
    try: 
        
        age = age
        
    except ValueError: 
        
        print("Invalid Response")