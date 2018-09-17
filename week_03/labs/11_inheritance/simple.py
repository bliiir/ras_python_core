class Grandparent():
    def __init__(self, other):
        self.age = 21
        self.col= other.col
        self.hair = other.hair

    def something(self):
        print("Hello")

class Parent(Grandparent):
    def __init__(self, age, col, hair):
        self.age = age
        self.col = col
        self.hair = hair
        Grandparent.__init__(self, self)

    #def something(self):
    #    print("World")

    pass


my_parent = Parent(34, "blue", "pink")
my_parent.something()
#my_parent.something()
print(vars(my_parent))
