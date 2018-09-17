'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

'''


class Car():
    """Class that creates car objects

    Attributes:
        fuels (list): A list of fuels that an object of type Car can be powered by
        makes (list): A list of makes that an object of type Car can be produced by
        shapes (list): A list of shapes that an object of type Car can take
        transmissions (list): A list of transmission types that an object of type Car can be equipped with

        make (INT): Integer referencing the makes list
        shape (INT): Integer referencing the shapes list
        transmission (INT): Integer referencing the transmissions list
        fuel (INT): Integer referencing the fuels list

        model (STR): The model of the car
        year (INT): Year of production
    """

    # Class attributes
    makes = ["Mercedes", "BMW", "Tesla"]
    shapes = ["coupe", "convertible", "station" ]
    transmissions = ["manual", "automatic", "stepless"]
    fuels = ["gasoline", "diesel", "electricity"]

    def __init__(self,make=0, shape=0, transmission=0, fuel=0, model="S class 450", year=2000):
        self.make = make
        self.shape = shape
        self.transmission = transmission
        self.fuel = fuel
        self.model = model
        self.year = year

    def __str__(self):
        specs = "make: {:10s} model: {:15} year: {:10}".format(self.makes[self.make], self.model, self.year)
        return(specs)

    def __add__(self, other):
        try:
            return(self.makes[self.make] + " and " + other.makes[other.make])
        except:
            print("something went wrong")

class House():
    """Class that makes very simple house objects

    Attributes:
        electricity_consumption (INT): Yearly consumption of electricirty in KWH
        type (list): Integer referencing the types list
    """

    # Class attributes
    types = ["Villa", "Bungalow", "Farmhouse"]

    # Init
    def __init__(self, type=0, electricity_consumption=1000):
        self.type = type
        self.electricity_consumption = electricity_consumption

    # print
    def __str__(self):
        specs = "type: {:10s} electricity consumption: {:10d}".format(self.types[self.type], self.electricity_consumption)
        return(specs)

    # + overload
    def __add__(self, other):
            return({"total_electricity":self.electricity_consumption + other.electricity_consumption})

class Computer():
    """Class that makes very-very simple computer objects

    Attributes:
        electricity_consumption (INT): Yearly consumption of electricirty in KWH
        type (list): Integer referencing the types list
    """

    # Class attributes
    types = ["laptop", "Desktop"]

    # Init
    def __init__(self, type=0, electricity_consumption=1000):
        self.type = type
        self.electricity_consumption = electricity_consumption

    # print
    def __str__(self):
        specs = "type: {:10s} electricity consumption: {:10d}".format(self.types[self.type], self.electricity_consumption)
        return(specs)

    # + overload
    def __add__(self, other):
            return({"total_electricity":self.electricity_consumption + other.electricity_consumption})

###########################
#### Make some objects ####
###########################

# Make some cars
car1 = Car()
car2 = Car(2,1,2,2, "Model S", 2018)

# Trigger the __str__ dunder method by printing the car objects
print(car1)
print(car2)

# Try the add method on the two car objects
print(car1 + car2)

# Change some properties in one of the car objects
car1.model = "Tincan"
car1.make = 1

# Print the car object that was changed
print(car1)

#####

# Make some Houses
house1 = House()
house2 = House(1, 5000)

# # Trigger the __str__ dunder method by printing the house objects
print(house1)
print(house2)

# Try the add method on the two house objects
print(house1 + house2)

# Change some properties in one of the house objects
house1.type = 2
house1.electricity_consumption = 10000

# Print the house object that was changed
print(house1)


####

# Make some computers
computer1 = Computer()
computer2 = Computer(1, 500)

# # Trigger the __str__ dunder method by printing the computer objects
print(computer1)
print(computer2)

# Try the add method on the two computer objects
print(computer1 + computer2)

# Change some properties in one of the computer objects
computer1.type = 1
computer1.electricity_consumption = 1000

# Print the computer object that was changed
print(computer1)
