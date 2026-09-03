def triangle():
    side1 = int(input("Enter the first side of triangle length: "))
    side2 = int(input("Enter the second side of triangle length: "))
    side3 = int(input("Enter the third side of triangle length: "))

    if side1+side2+side3 == 180:
        print("It can be a rectangle")
    else:
        print("It cannot be a rectangle")


triangle()

