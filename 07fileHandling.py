#! /usr/bin/python3

#writing data to a file
def writeToFile(filename: str) -> None:
    data = "This is an example text to write into a file."
    
    # use try and except so that if the program crashes, it'll close
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(f"Data has been written to {filename}")
    except:
        print(f"Error. Could not write to {filename}")

#reading data from a file
def readFromFile(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(f"data read from {filename}")
            print(data)
    except:
        print(f"Error. Could not write to {filename}")

#appending data to a file
def appendToFile(filename: str, newData: str) -> None:
    try:
        with open(filename, "a") as file:
            file.write("\n" + newData)
        print(f"Data appended to {filename}")
    except:
        print(f"Error. Could not write to {filename}")

def main() -> None:
    filename: str = "07Sample.txt"

    writeToFile(filename)
    readFromFile(filename)

    newData: str = "This is a new data set appended to the file lol"
    appendToFile(filename, newData)

    readFromFile(filename)

if __name__ == "__main__":
    main()

# Output:
# Data has been written to 07Sample.txt
# data read from 07Sample.txt
# This is an example text to write into a file.
# Data appended to 07Sample.txt
# data read from 07Sample.txt
# This is an example text to write into a file.
# This is a new data set appended to the file lol
