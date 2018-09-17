## Classes and OOP

- What is a class?

        A programmer defined type - just like a string class, but with properties specific to

- How do you define a new class called `MyFirstClass`?

        Class MyFirstClass():

            def __init__(self, ...):
                ...

- How do you create an object of the class `MyFirstClass`?

        my_first_instance = MyFirstClass(...)

- What is instantiation?

        The act of creating an object from a class

- What are attributes?

        Named elements of an object

- What does it mean when an object is embedded?

        That the object is an attribute of another object

- What is the difference between `copy.copy` and `copy.deepcopy`?
What do they each do?

        copy.copy copies an object without its embedded objects and copy.deepcopy copies it with the embedded objects

- What is the difference between a pure function and a modifier?

        A pure function does not modify any of the objects passed to it as arguments and it has no effect, like displaying a value or getting user input, other than returning a value.

        A modifier does one or all of these things.

- What is object-oriented programming?

        OOP has these defining characteristics:

            - Programs include class and method definitions.
            - Most of the computation is expressed in terms of operations on objects.
            - Objects often represent things in the real world, and methods often correspond to the ways things in the real world interact.


## Methods (page 161)

- What is a method?

        A method is a function that is associated with a particular class

- How is a method different than a function?

        - Methods are defined inside a class definition in order to make the relationship between the class and the method explicit.
        - The syntax for invoking a method is different from the syntax for calling a function.

- What is invocation?

        Calling or activting the method

- What is the `__init__` method and what is it used for?

    It is the method



- Give an example `__init__` method for a `Car` class with attributes:
`make`, `model` and `year.

        class Car():
            def __init__(self, make, model, year):
                self.make = make
                self.model = model
                self.year = year


- How do `__init__` methods handle variable arguments?

        It assigns them to the object on instantiation


- What is the `__str__` method used for?

        To represent the object as a string. `obj.__str__()` is invoked with the `print(obj)` command

- How do you use a `__str__` method?

        See above

- What is operator overloading?

        Changing the behavior of an operator like + so it works with a programmer-defined type.



- What is an example of operator overloading?

        class my_class();

                    def __init__(self, num):
                        self.num = num

                    def __add__(self, num)
                        return(self.num + num)


## TYPE-BASED DISPATCH?

        A programming pattern that checks the type of an operand and invokes different functions for different types.

- What is polymorphism?

        Functions that work with several types are called polymorphic


- Why is polymorphism beneficial?

        Polymorphism can facilitate code reuse
