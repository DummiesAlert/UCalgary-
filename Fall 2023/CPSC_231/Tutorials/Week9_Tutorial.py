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

# control = True  # Set control to True initially

# def student(): 
    
#     WTAAS = input("Want to Add a Student? ")
#     WTAAS.lower()
    
#     if WTAAS == 'yes': 
        
#         return True
    
#     else: 
        
#         return False

# def again():
    
#     again = input("Want to Add Another Student? (Yes to Continue, Quit to End) ")
#     again.lower()
    
#     if again == 'quit': 
        
#         return False  # Set control to False if user wants to quit
    
#     elif again == 'yes': 
        
#         main()
    
#     elif again != 'yes': 
        
#         print("Please Try Again!!!")
#         return again()
    
# def main(): 
    
#     student()
#     count = 4
    
#     while control: 
#         name = input("Enter Name to Add: ")
#         year = input("Enter Year to Add: ")

#         STUDENTS = {
#             "Student1": "Jose", 
#             "Year1": "2032", 
#             "Student2":"Gordon", 
#             "Year2":"2034", 
#             "Student3": "Charls", 
#             "Year3": "2038"
#         }

#         STUDENTS["Student"+str(count)] = name
#         STUDENTS["Year"+str(count)] = year

#         control = again()  # Update control based on user's input

#         count += 1

# main()

students = []

def student():
    return input("Want to Add a Student? (Yes/No): ").lower() == 'yes'

def main():
    while student():
        name = input("Enter Name to Add: ")
        year = input("Enter Year to Add: ")
        students.append({"name": name, "year": year})
    
    print("Students added:")
    for i, student in enumerate(students, start=1):
        print(f"Student{i}: {student['name']}, Year: {student['year']}")

main()