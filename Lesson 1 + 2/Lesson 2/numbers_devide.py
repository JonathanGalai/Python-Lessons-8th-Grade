number = int(input("Enter a number: "))
isPrime = True
for i in range(number//2):
    tmp = i+2
    if number % tmp == 0:
        print(tmp)
        isPrime = False

if isPrime == True:
    print(number, "is a prime number")