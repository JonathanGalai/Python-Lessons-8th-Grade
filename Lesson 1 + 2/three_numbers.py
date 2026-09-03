def numbers():
    number1 = int(input("Enter your first number: "))
    number2 = 10-number1
    if number1 < number2:
        number3 = number2 - number1
    else:
        number3 = number1 - number2

    print("The number is: ",number1, number2, number3)
numbers()