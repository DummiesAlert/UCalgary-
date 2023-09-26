# Write a Program that Checks if a number entered by the user is divisible by both 2 and 3, or either of them. 

a = int(input("Enter a Number: "))

try: 
    if a > 0: 
        if (a % 2 == 0) and (a % 3 == 0): 
    
            print("It is Divisible by 2 and 3!!")
        
        elif (a % 2 == 0): 
        
            print("It is Divisible by 2!!")
    
        elif (a % 3 == 0): 
    
            print("It is Divisible by 3!!")
    
        elif not(a % 2 == 0) and not(a % 3 == 0): 
    
            print("It is NOT Divisible by 2 and 3!!")
            
except ValueError: 
    
    print("NOT A NUMBER DUMMIE")