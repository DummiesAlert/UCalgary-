# Important note: use at your own risk. This is meant as a guide only and does not
# represent your official grade. The teaching team is not responsible for errors in this code.
# It does not take into account any bonus, or excused absences, or other special cases.

import numpy as np

print("Enter your letter grades for each.")
a1 = input("Please enter your letter for assignment1: ")
a2 = input("Please enter your letter for assignment2: ")
a3 = input("Please enter your letter for assignment3: ")
a4 = input("Please enter your letter for assignment4: ")
exam1 = input("Please enter your letter for exam1: ")
exam2 = input("Please enter your letter for exam2: ")
exam3 = input("Please enter your letter for exam3: ")
final = input("Please enter your letter for final exam: ")

converter = {"A+": 4, "A": 4, "A-": 3.7,
             "B+": 3.3, "B": 3, "B-": 2.7,
             "C+": 2.3, "C": 2, "C-": 1.7,
             "D+": 1.3, "D": 1, "F": 0}

lst = [a1, a2, a3, a4, exam1, exam2, exam3, final]
print("Letter grades: ", lst)

lst_gp = []
for item in lst:
    if item.upper() in converter:
        lst_gp.append(converter[item.upper()])
    else:
        print("Invalid letter grade entered.")
        lst_gp.append(-1000)
print("Grade points: ", lst_gp)

weights = [0.03, 0.04, 0.04, 0.05, 0.18, 0.18, 0.18, 0.3]
combined = np.dot(lst_gp, weights)
if final.upper() == "D":
    combined = min(combined, 1)
elif final.upper() == "F":
    combined = 0
print("Combined grade points: %.3f" % combined)

letter_grade = "F"
if combined > 3.85:
    letter_grade = "A or A+"
elif combined > 3.5:
    letter_grade = "A-"
elif combined > 3.15:
    letter_grade = "B+"
elif combined > 2.85:
    letter_grade = "B"
elif combined > 2.5:
    letter_grade = "B-"
elif combined > 2.15:
    letter_grade = "C+"
elif combined > 1.85:
    letter_grade = "C"
elif combined > 1.5:
    letter_grade = "C-"
elif combined > 1.15:
    letter_grade = "D+"
elif combined > 0.5:
    letter_grade = "D"

print("Round and convert back to letter grade: ", letter_grade)
print("The letter grade is the only grade that will appear on your transcript.")

print("\nImportant note: use at your own risk. This is meant as a guide only and does not")
print("represent your official grade. The teaching team is not responsible for errors in this code.")
print("It does not take into account any bonus, or excused absences, or other special cases.")
