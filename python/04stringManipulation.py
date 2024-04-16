#! /usr/bin/python3

def stringManipulation(userString:str) -> None:
    #Length of a string
    print(f"Length of string: {len(userString)}")
    
    # NOTE: the first character is a 0.
    # Accessing characters in a string
    print(f"First character: {userString[0]}")
    print(f"Last character: {userString[-1]}")

    #slicing
    print(f"Substring from index 7-12: {userString[7:12]}")

    #Connecting strings
    str1 = "hello"
    str2 = "world"
    connectedString = str1 + "," + str2 + "!"
    print(f"Connected string: {connectedString}")

    #String methods
    #Lowercase
    print(f"Lowercased string: {userString.lower()}")
    #Uppercase
    print(f"Uppercase string: {userString.upper()}")
    #Capitalise
    print(f"Capitalised string: {userString.capitalize()}")

    #Count occurences of a substring
    substring = "sample"
    #.format() changes the things INSIDE {} in the print string statement to whatever is inside the .format() function
    print("Occurences of '{}' in the string:".format(substring), userString.count(substring))

    # Find index of a substring
    print(f"index of {substring} in the string:", userString.find(substring))

    # Replace a string
    oldSubstring = "sample"
    newSubstring = "example"
    print("String after replacement:", userString.replace(oldSubstring, newSubstring))

    # Split a string into a list
    words = userString.split(" ")
    print(f"Words in the string: {words}")

    # Join elements of a list into a string
    jointString = "-".join(words)
    print(f"Joined string with '-': {jointString}")

def main():
    userString = "Hello World! This is a sample string for the string manipulation lesson!"
    stringManipulation(userString)

if __name__ == "__main__":
    main()

#Output

# Length of string: 72
# First character: H
# Last character: !
# Substring from index 7-12: orld!
# Connected string: hello,world!
# Lowercased string: hello world! this is a sample string for the string manipulation lesson!
# Uppercase string: HELLO WORLD! THIS IS A SAMPLE STRING FOR THE STRING MANIPULATION LESSON!
# Capitalised string: Hello world! this is a sample string for the string manipulation lesson!
# Occurences of 'sample' in the string: 1
# index of sample in the string: 23
# String after replacement: Hello World! This is a example string for the string manipulation lesson!
# Words in the string: ['Hello', 'World!', 'This', 'is', 'a', 'sample', 'string', 'for', 'the', 'string', 'manipulation', 'lesson!']
# Joined string with '-': Hello-World!-This-is-a-sample-string-for-the-string-manipulation-lesson!
