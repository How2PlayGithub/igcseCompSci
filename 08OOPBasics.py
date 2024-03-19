#! /usr/bin/python3

class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        # Constructor method to initialise a Car object with attributes given
        # which are brand, model, year and color

        #assigning values to instance variables
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.mileage: float = 0

    def displayInformation(self) -> None:
            print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}")
        
    def drive(self, distance: float) -> None:
            #updating mileage
            self.mileage += distance
            print(f"The car has driven {distance} miles.")

    def getMileage(self) -> float:
            return self.mileage

def main() -> None:
    # creating instances of Car class
    toyotaCamry: Car = Car("Toyota", "Camry", 2020, "Red")
    hondaAccord: Car = Car("Honda", "Accord", 2019, "Blue")

    # displaying car information
    print("Toyota Camry Information:")
    toyotaCamry.displayInformation()
    print("Honda Accord Information:")
    hondaAccord.displayInformation()

    # "driving" the cars
    toyotaCamry.drive(50)
    hondaAccord.drive(70)

    # displaying the mileage
    print("Toyota Camry Mileage: ", toyotaCamry.getMileage())
    print("Honda Accord Mileage: ", hondaAccord.getMileage())

if __name__ == "__main__":
    main()

# Output:
# Toyota Camry Information:
# Brand: Toyota, Model: Camry, Year: 2020, Color: Red
# Honda Accord Information:
# Brand: Honda, Model: Accord, Year: 2019, Color: Blue
# The car has driven 50 miles.
# The car has driven 70 miles.
# Toyota Camry Mileage:  50
# Honda Accord Mileage:  70
