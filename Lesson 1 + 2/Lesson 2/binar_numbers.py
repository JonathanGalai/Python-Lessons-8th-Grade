number = int(input("Enter a binary number: "))
original = number
isBinary = True

if number == 0:
    isBinary = True
else:
    while number > 0:
        digit = number % 10
        if digit != 0 and digit != 1:
            isBinary = False
        number = number // 10

if isBinary:
    print(original, "is binary")
else:
    print(original, "is not binary")