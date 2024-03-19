#! /usr/bin/python3

def conditionalStatements(number: int) -> None:
    # if statement
    if number > 0:
        print("The number is positive")
    # elif statement (else if)
    elif number < 0:
        print("The number is negative")
    elif number == 0:
        print("The number is zero")
    # else (statement IF error)
    else:
        print("unknown number")

def forAndWhileLoops(numberFactorial: int) -> None:
    # FOR loop example
    # Count-controlled
    print("Printing numbers from 1 to 5 using a FOR loop:")
    # We use '6' because the comupter ENDS at 6. 
    # You could also start at 0 and end at 5.
    for i in range(1, 6):
        print(i, end = " ")
    print()
    
    # WHILE loop example
    # Conditional loop
    print("Finding factorial of a number")
    factorial = 1
    while numberFactorial > 0:
        factorial *= numberFactorial
        numberFactorial -= 1
    print(f"The factorial is {factorial}")
    
    # Loop control statements
    for i in range(1,11):
        # it'll only print 1, 2, 3, 4
        if i == 5:
            break
        print(i, end=" ")

def main() -> None:
    controlNumber = 5
    conditionalStatements(controlNumber)
    forAndWhileLoops(controlNumber)
    print()

if __name__ == "__main__":
    main()

# Output:
# The number is positive
# Printing numbers from 1 to 5 using a FOR loop:
# 1 2 3 4 5
# Finding factorial of a number
# The factorial is 120
# 1 2 3 4
