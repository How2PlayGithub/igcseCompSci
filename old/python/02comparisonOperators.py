#! /usr/bin/python3

def comparisonOperatiors(userInputOne: int, userInputTwo: int) -> None:
    # This is the 'is equal' comparison
    userInputOne = 1
    userInputTwo = 1
    if userInputOne == userInputTwo:
        print(f"the 'is equal' comparison (==)")
    #The next one is 'not equal'
    userInputOne = 1
    userInputTwo = 2
    if userInputOne != userInputTwo:
        print(f"the 'not equal' comparison (!=)")
    #This is the greater than comparison
    if userInputTwo > userInputOne:
        print(f"the 'greater than' comparison (>)")
    #This is the smaller than comparison
    if userInputOne < userInputTwo:
        print(f"the 'smaller than' comparison (<)")
    # The last are basically greater or equal to, and smaller or equal to
    if userInputOne <= userInputTwo:
        print(f"the 'smaller or equal to' comparison (<=)")
    if userInputTwo >= userInputOne:
        print(f"the 'greater or equal to' comparison (>=)")

def main():
    # we don't really need to set values, as we have hard coded it
    # in the function
    comparisonOperatiors(0, 0)

if __name__ == "__main__":
    main()

#Output:
# the 'is equal' comparison (==)
# the 'not equal' comparison (!=)
# the 'greater than' comparison (>)
# the 'smaller than' comparison (<)
# the 'smaller or equal to' comparison (<=)
# the 'greater or equal to' comparison (>=)
