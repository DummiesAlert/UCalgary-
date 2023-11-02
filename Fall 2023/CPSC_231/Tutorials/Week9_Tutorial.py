"""

    Learn how to use split()
    Dictionary, exsting and non-existing key values

        If you want to call a value, cannot be after the colon. 
    
        q_and_a = \
        {
            "name": "I am Chat231. My nickname is Riley.",
            "textbook": "The textbook we use is called The Python Workbook 2nd Edition.",
            "break": "Fall break is November 13th to 17th.",
            "deadline": "This assignment is due on November 10th.",
            "final exam": "The final exam will be on December 18th at 5-7pm. Check D2L for details."
        }

"""

#Example: 

def student(): 

    WTAAS = input("Want to Add a Student? ")
    WTAAS = WTAAS.lower()

    if WTAAS == 'yes': 

        return True
    
    else: 
    
        return False

def again():

    again = str(input("Want to Add Another Student? (Yes to Continute, Quit to End) "))
    again = again.lower()
    
    if again == 'quit': 

        False

    elif again != 'yes': 

        print("Please Try Again!!!")
        again = str(input("Want to Add Another Student? (Yes to Continute, Quit to End) "))
        again = again.lower()

student()

count = 4
control = False

while control == True: 

    name = str(input("Enter Name to Add: "))
    year = str(input("Enter Year to Add: "))

    STUDENTS = \
    {
        
        "Student1": "Jose", 
        "Year1": "2032", 
        "Student2":"Gordon", 
        "Year2":"2034", 
        "Student3": "Charls", 
        "Year3": "2038"
        
    }

    STUDENTS[count] = {"Student"+str(count): name, "Year"+str(count): year}

    again()

    count += 1