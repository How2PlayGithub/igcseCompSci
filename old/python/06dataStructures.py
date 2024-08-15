#! /usr/bin/python3

def lists() -> None:
    myList = [1,2,3,4,5]
    print(f"Original list: {myList}")

    #accessing elements
    print(f"First element: {myList[0]}")
    print(f"Last element: {myList[-1]}")

    #adding elements
    myList.append(6)
    print(f"After adding 6: {myList}")

    #removing elements
    myList.remove(6)
    print(f"After removing 6: {myList}")

    #popping elements
    poppedElement =  myList.pop()
    print(f"Popped element: {poppedElement}")
    print(f"List after popping: {myList}")

def tuples() -> None:
    print("\nTuples:")
    myTuple = (1,2,3,4,5)
    print(f"Original tuple: {myTuple}")

    #accessing elements
    print(f"First element: {myTuple[0]}")
    print(f"First element: {myTuple[-1]}")

    #note that tuples are IMMUTABLE (unchangeable)

def dictionaries() -> None:
    print("\nDictionaries:")
    myDictionary = {"name": "Putin", "age": 71, "city": "Moscow"}
    print(f"Original dictionary: {myDictionary}")

    #accessing elements
    print(f"Name: {myDictionary['name']}")
    print(f"Age: {myDictionary['age']}")
    print(f"City: {myDictionary['city']}")

    #dictionary methods
    print(f"Keys: {myDictionary.keys()}")
    print(f"Values: {myDictionary.values()}")
    print(f"Items: {myDictionary.items()}")

def sets() -> None:
    print("\nSets:")
    mySet1 = {1,2,3,4,5}
    mySet2 = {4,5,6,7,8}

    #adding elements
    mySet1.add(6)
    print(f"After adding 6 to Set 1: {mySet1}")

    #removing elements
    mySet1.remove(6)
    print(f"After removing 6 from Set 1: {mySet1}")

    #set operations
    print(f"Union: {mySet1.union(mySet2)}")
    print(f"Intersection: {mySet1.intersection(mySet2)}")

def main() -> None:
    lists()
    tuples()
    dictionaries()
    sets()

if __name__ == "__main__":
    main()

# Output:
# Original list: [1, 2, 3, 4, 5]
# First element: 1
# Last element: 5
# After adding 6: [1, 2, 3, 4, 5, 6]
# After removing 6: [1, 2, 3, 4, 5]
# Popped element: 5
# List after popping: [1, 2, 3, 4]
#
# Tuples:
# Original tuple: (1, 2, 3, 4, 5)
# First element: 1
# First element: 5
#
# Dictionaries:
# Original dictionary: {'name': 'Putin', 'age': 71, 'city': 'Moscow'}
# Name: Putin
# Age: 71
# City: Moscow
# Keys: dict_keys(['name', 'age', 'city'])
# Values: dict_values(['Putin', 71, 'Moscow'])
# Items: dict_items([('name', 'Putin'), ('age', 71), ('city', 'Moscow')])
#
# Sets:
# After adding 6 to Set 1: {1, 2, 3, 4, 5, 6}
# After removing 6 from Set 1: {1, 2, 3, 4, 5}
# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
