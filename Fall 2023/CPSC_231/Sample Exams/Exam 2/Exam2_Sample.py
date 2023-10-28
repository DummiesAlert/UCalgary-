# Question 1: 

# year and colour are two variables with values assigned previously 

# if year < 2000 and colour == "Blue": 
#     print("Invalid.") 
#     exit() 
# print("Good!")

# if year > 2000 and colour != "Blue":

#     print("Good!")

# else: 

#     print("Invalid.")

# Question 2: Decreasing Order

numRows = int(input("Enter the Amount of Rows!!"))

for i in range(0, numRows): 
    for j in range(numRows, i , -1): 

        print("* ", end = "")

    print(" ")
    
numRows = int(input("Enter the Amount of Rows!!"))

i = 0
while i < numRows:
    j = numRows
    while j > i:
        print("* ", end = "")
        j -= 1
    print(" ")
    i += 1
    
# Question 2: Increasing 

numRows = int(input("Enter the Amount of Rows!!"))

for i in range(0, numRows):
    for j in range(0, i + 1):
        
        print("* ", end="")
        
    print(" ")