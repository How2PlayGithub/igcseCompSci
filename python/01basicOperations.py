#! /usr/bin/python3

# Let's start with python operations!
def pythonOperations(inputOne: int, inputTwo: int) -> None :
    output = 0
    # To add, use +
    output = inputOne + inputTwo
    print(f"this is the addition function (+): {output}")
    # To subtract, use -
    output = inputOne - inputTwo
    print(f"this is the subtract function (-): {output}")
    # To multiply, use *
    output = inputOne * inputTwo
    print(f"this is the multiply function (*): {output}")
    # To divide, use /
    output = inputOne / inputTwo
    print(f"this is the divide function (/): {output}")
    # To do poewrs, use **
    output = inputOne ** inputTwo
    print(f"this is the power function (**): {output}")

    # Here are the unusual ones
    # Modulus --> gives the remainder
    output = inputOne % inputTwo
    print(f"this is the modulus function (%): {output}")
    #Floor division --> ignores decimals when dividing
    output = inputOne // inputTwo
    print(f"this is the floor division function (//): {output}")

# Let's test our function!

def main() -> None:
    userInputOne = int(input("Enter a integer: "))
    userInputTwo = int(input("Enter a integer: "))
    pythonOperations(userInputOne, userInputTwo)

if __name__ == "__main__":
    main()
# The output is:
# this is the addition function (+): 10
# this is the subtract function (-): -4
# this is the multiply function (*): 21
# this is the divide function (/): 0.42857142857142855
# this is the power function (**): 2187
# this is the modulus function (%): 3
# this is the floor division function (//): 0
