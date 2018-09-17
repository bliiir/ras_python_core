'''
Build on 10_03_freeform_classes from the section on Classes, Objects and
Methods.
Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in 10_03_freeform_classes.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''


class Car():
    """Class that creates car objects

    Attributes:
        fuels (LIST):           A list of fuels that an object of type Car can be powered by
        makes (LIST):           A list of makes that an object of type Car can be produced by
        shapes (liLISTst):      A list of shapes that an object of type Car can take
        transmissions (LIST):   A list of transmission types that an object of type Car can be equipped with

        make (INT):             Integer referencing the makes list
        shape (INT):            Integer referencing the shapes list
        transmission (INT):     Integer referencing the transmissions list
        fuel (INT):             Integer referencing the fuels list

        model (STR):            The model of the car
        year (INT):             Year of production
    """

    # Class attributes
    shapes = ["coupe", "convertible", "station" ]
    transmissions = ["manual", "automatic", "stepless"]
    fuels = ["gasoline", "diesel", "electricity"]

    def __init__(self,
        shape=0,
        transmission=0,
        fuel=0,

        wheels = 4,
        doors = 5,
        hp = 150):

        self.shape = shape
        self.transmission = transmission
        self.fuel = fuel
        self.wheels = wheels
        self.doors = doors
        self.hp = hp

    def __str__(self):
        specs = "shape: {:10s} transmission: {:15} fuel: {:10} wheels: {:10} doors: {:10} horse-power: {:10}".format(self.shapes[self.shape], self.transmissions[self.transmission], self.fuels[self.fuel], self.wheels, self.doors, self.hp)
        return(specs)

    def __add__(self, other):
            # Returns total horsepower of the two car objects
            return(self.hp + other.hp)


class Musclecar(Car):

    """Creates a musclecar

    Attributes:
        makes (LIST): Class attribute list with possible makes of the musclecars
        make (INT): An integer referencing the makes list
        rimsize (): The size of the musclecars rims
    """

    makes = ["Dodge", "Ford", "Buick"]

    def __init__(self, make=0, rimsize=16):
        Car.__init__(self, shape=1, transmission=0, fuel=0, wheels=4, doors=2, hp=400)
        self.make = make
        self.rimsize = rimsize

    def __str__(self):
        specs = "make: {:10s}".format(self.makes[self.make], self.transmissions[self.transmission])
        return(specs)

class Hotrod(Musclecar):

    def __init__(self, color):
        Musclecar.__init__(self, make=2, rimsize=18)
        self.color = color


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

class Villa(House):

    def __init__(self, roofing):
        self.roofing = roofing





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

my_musclecar = Musclecar(1)
print(my_musclecar)

my_hotrod = Hotrod("Blue")
print(my_hotrod)

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
