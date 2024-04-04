# M03 Lab - Case Study: Lists Functions, and Classes

# Firisiya Chiomadzi
# 04/04/2024

# A Python app that has a super class called Vehicle, which contains an attribute for a car,
# and a class called Automobile which will inherit the attributes from "Vehicle" containing,
# the year, make, model, doors (2 or 4), and roof (solid or sunroof).

# The App will accept user input for a car, store "car" into the vehicle type in the super class.
# The app will then ask the user for the year, make, model, doors, and type of roof and store that
# data in the attributes above, and output the data.

# Define the Vehicle class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile class inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to accept user input and create a car object
def create_car():
    print("Please enter the details for your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sunroof): ")
    car = Automobile("car", year, make, model, doors, roof)
    return car

# Function to display car details
def display_car(car):
    print("\nVehicle type:", car.vehicle_type)
    print("Year:", car.year)
    print("Make:", car.make)
    print("Model:", car.model)
    print("Number of doors:", car.doors)
    print("Type of roof:", car.roof)

# Main function
def main():
    car = create_car()
    display_car(car)

if __name__ == "__main__":
    main()