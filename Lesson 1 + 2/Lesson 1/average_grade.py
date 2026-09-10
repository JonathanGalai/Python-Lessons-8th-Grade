def calculate_grade():
    math = int(input("Enter your math grade: "))
    science = int(input("Enter your science grade: "))
    english = int(input("Enter your english grade: "))
    sport = int(input("Enter your sport grade: "))

    print("Your average grade is: ", (math+science+english+sport)/4)

calculate_grade()