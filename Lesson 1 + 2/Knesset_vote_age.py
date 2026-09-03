def knesset():
    age = int(input("Can you vote for Knesset? In which Year were you born? "))
    year = int(input("What is this year's number? "))

    if year - age > 18:
        print("You can vote for knesset!")
    else:
        print("You can't vote for knesset.")

knesset()