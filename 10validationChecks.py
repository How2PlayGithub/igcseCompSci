#! /usr/bin/python3

# Imports
import re

def validateCheck(inputData) -> tuple[bool, str]:
    # Type validation
    if not isinstance(inputData, (int, float)):
        return False, "Input must be a number"

    # Value-range validation
    if inputData < 0 or inputData > 100:
        return False, "Input must be between 0 and 100"

    # Presence check
    if inputData is None:
        return False, "Input can't be None"

    # Fomat validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", str(inputData)):
        return False, "Invalid email address format."

    # Length validation
    if len(str(inputData)) < 5 or len(str(inputData)) > 20:
        return False, "Input length must be between 5 and 20 characters"

    # Custom validation
    if inputData % 5 != 0:
        return False, "Input must be divisible by 5"

    # Dependancy Validation
    inputDataTwo = 30
    if inputData > 50 and inputDataTwo is None:
        return False, "Another input is required that is greater than 50"

    return True, "Validation successful"

def testValidations() -> None:
    inputNumber = 75
    emailAddress = "example@example.com"

    message = validateCheck("not a number")
    print(message)
    message = validateCheck(inputNumber)
    print(message)
    message = validateCheck(emailAddress)
    print(message)
    message = validateCheck(inputNumber)
    print(message)

def main() -> None:
    testValidations()

if __name__ == "__main__":
    main()

# Output:
# (False, 'Input must be a number')
# (False, 'Invalid email address format.')
# (False, 'Input must be a number')
# (False, 'Invalid email address format.')

