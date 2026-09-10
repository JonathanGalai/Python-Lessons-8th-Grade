import random

gradeList = [random.randint(1,100) for i in range(0,20)]
honorStudents = [grade for grade in gradeList if grade > 85]
print("All grades: ", gradeList)
print("Best scores", honorStudents)
