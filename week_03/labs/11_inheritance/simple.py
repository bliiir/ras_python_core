class Parent():

"""
Creates a parent object

A bit longer description.

Args:
    variable (type): description

Returns:
    type: description

Raises:
    Exception: description

"""

    # Class attributes - these are the genes of the class. All children will have them
    species = "Human"
    planet = "Earth"

    # Instance attributes - all instences of the class will have these, but not its children unless this init is triggered from the child
    def __init__(self, name, birthyear, skin, hair, height=200):
        self.name = name
        self.birthyear = birthyear
        self.skin = skin
        self.hair = hair
        self.height = height

class Child(Parent):

    def __init__(self, father, mother, name, birthyear):
        # This init function forwards the attributes passed to this child to the parent and the variables are embedded in the child
        Parent.__init__(self, father.name, father.birthyear, father.skin, father.hair, father.height)
        super(Child, self).
        self.name = name
        self.birthyear = birthyear

mother = Parent("Jette", "1949", "white", "light-blonde", "157")
father = Parent("Alf", "1948", "white", "dark-blonde", "205")
son = Child(father, mother, "Rasmus", "1975")

print(vars(mother))
print(vars(father))
print(vars(son))

son.height = "189"

print(vars(son))

## Questions
# - how do I make a daughter who inherits from Mother? Not instanciate a new mother, but from the actual mother object?
