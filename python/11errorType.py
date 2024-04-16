#! /usr/bin/python3

# syntax error
# an error which violates syntax rules
def syntaxError() -> None:
    if x == 5 # missing colon
        print("x is 5")

# logic errors / semantic errors
def logicError() -> None:
    results = 0
    for i in range(1, 11):
        results += i
        if i == 5: # incorrect condition
            results -= i # incorrect condition
    print(results)

# runtime errors
def runtimeError() -> None:
    x = 10
    y = 0
    result = x / y
    print(result) # cannot divide by 0
