name = input("Enter Your Name: ")
# input subjects
math = int(input("Enter Math Marks: "))
phy = int(input("Enter Physics Marks: "))
che = int(input("Enter Chemistry Marks: "))
eng = int(input("Enter English Marks: "))
hin = int(input("Enter Hindi Marks: "))
 
# Calculate total marks
total = math + phy + che + eng + hin
percentage = (total / 500) * 100
def grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"
def result(percentage):
    if percentage >= 60:
        return "Pass"
    elif percentage >= 45:
        return "Second Division"
    elif percentage >= 33:
        return "Third Division"
    else:
        return "Fail"
marks_list = [math, phy, che, eng, hin]
highest_marks = max(marks_list)
lowest_marks = min(marks_list)

if percentage >= 33:
    bonus_marks = 5
else:
    bonus_marks = 0
bonus_total = total + bonus_marks
bonus_percentage = (bonus_total / 500) * 100

# --- PRINTING THE MARKSHEET ---
print("\n================ STUDENT MARKSHEET ================")
print(f"Student Name     : {name}")
print(f"Total Marks      : {total} / 500")
print(f"Percentage       : {percentage:.2f}%")
print(f"Grade            : {grade(percentage)}")
print(f"Division Status  : {result(percentage)}")
print("---------------------------------------------------")
print(f"Highest Marks    : {highest_marks}")
print(f"Lowest Marks     : {lowest_marks}")
print("---------------------------------------------------")
print(f"Bonus Marks Given: {bonus_marks}")
print(f"Bonus Total      : {bonus_total} / 500")
print(f"Bonus Percentage : {bonus_percentage:.2f}%")
print(f"Final Grade      : {grade(bonus_percentage)}")
print("===================================================")