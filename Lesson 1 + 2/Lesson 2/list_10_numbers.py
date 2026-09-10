import random

gradeList = [random.randint(1, 100) for i in range(10)]
print(gradeList)

maxGrade = gradeList[0]
minGrade = gradeList[0]

for grade in gradeList:
    if grade > maxGrade:
        maxGrade = grade
    if grade < minGrade:
        minGrade = grade

print("Max:", maxGrade)
print("Min:", minGrade)