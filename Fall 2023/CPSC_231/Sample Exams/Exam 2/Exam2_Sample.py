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

# Question 2: 

numRows = int(input("Enter the Amount of Rows!!"))

for i in range(0, numRows): 
    for j in range(numRows, i , -1): 

        print("* ", end = "")

    print()