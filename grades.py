import sys
student = ""
gradebook = {}

print("Enter XXX to stop entering students.")

while student != "XXX":
    student = raw_input("Name: ")
    if (student != "XXX"):
        grade = int(raw_input("Grade: "))
        gradebook.update({student:grade})
    if (student == "XXX" and gradebook == {}):
        print("\n\tExiting without changes.\n")
        sys.exit()
    print("\n")


print("| Student\t| Grade\t|")
print("+++++++++++++++++++++++++")
bestStudent = ""
bestGrade = 0
worstStudent = ""
worstGrade = 100
totalGrades = 0
numGrades = 0

for student, grade in gradebook.items():
    print("| " + student + "\t| " + str(grade) + "\t|")
    if (grade > bestGrade):
        bestGrade = grade
        bestStudent = student
    if (grade < worstGrade):
        worstGrade = grade
        worstStudent = student
    totalGrades = totalGrades + grade
    numGrades = numGrades + 1
averageGrade = totalGrades/numGrades


print("\n\tBest Student: " + bestStudent + " / Grade: " + str(bestGrade))
print("\n\tStudent who needs most improvement: " + worstStudent + " / Grade: " + str(worstGrade))

print("\nAverage Grade: " + str(averageGrade))
