def difference_numbers():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if number1 > number2:
        print("The difference is ", number1 - number2)
    else:
        print("The difference is ", number2 - number1)

difference_numbers()