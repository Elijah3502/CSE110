"""
Team Activity
Week 05
Purpose: Compute and display letter grades after receiving an input on grade percentage
"""
print("Let's calculate your letter grade and check if you passed this class")
#gather input on grade percentage
grade = int(input("Please enter here your grade percentage: "))
#Calculate and present letter grade from A - F using if, elif and else statements.
# A >= 90 | B >= 80 | C >= 70 | D >= 60 | F < 60
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
#output letter grade
print(f"Your letter grade is: {letter_grade}")
#Display if student passed the class | must have at least a 70 to pass the class
if grade >= 70:
    print("Great job! You passed the class!")
else:
    print("You didn't pass the class this time. But don't give up! With hard work you will surely pass it next time.")