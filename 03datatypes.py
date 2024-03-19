#! /usr/bin/python3

#Here are the basic datatypes
def pythonDatatypes() -> None:
    typeString:str= 'hello world'
    typeInt:int = 3
    typeFloat:float = 3.1278312
    typeBool:bool = True
    # To test what type, use the type() function
    print(type(typeString))
    print(type(typeInt))
    print(type(typeFloat))
    print(type(typeBool))

def main() -> None:
    pythonDatatypes()

if __name__ == "__main__":
    main()
 
#Output:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
