class Grandparent():
    #height = 45
    def __init__(Ras, Adwan):
        self.age = 23
        self.col= "white"
        self.hair = "Black"

    # def something(self):
    #     print("Hello")

class Parent(Grandparent):
    def __init__(self):
        Grandparent.__init__(adwan, ras)
        self.kindness = 2
        #self.col = col
        #self.hair = hair


    #def something(self):
    #    print("World")

    pass


my_parent = Parent()
#my_parent.something()
#my_parent.something()
print(vars(my_parent))
#print(my_parent.height)
