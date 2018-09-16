'''
Work through the chapter "Classes and Objects" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2016.html and
build out the Point class example.

The provided code to start is in file Point1.py in this folder.

'''

from __future__ import print_function, division


class Point:
    """Represents a point in 2-D space.

    Attributes:
        x (Float): x-coordinate
        y (Float): y-coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        #Print a Point object in human-readable format.
        return('(%g, %g)' % (self.x, self.y))


class Rectangle():

    """Represents a rectangle.

    Attributes:
        corner (OBJ): Top left corner
        height (FLOAT): Height of the rectangle
        width (FLOAT): Width of the rectangle
    """

    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

    def get(self):
        return({"x":self.corner.x, "y":self.corner.y, "w":self.width, "h":self.height})


    def find_center(self):
        """Returns a Point at the center of a Rectangle.

        self: Rectangle

        returns: center Point
        """
        return(Point(self.corner.x + self.width/2.0, self.corner.y + self.height/2.0))


    def grow_rectangle(self, dwidth, dheight):
        """Modifies the Rectangle by adding to its width and height.

        self: Rectangle object.
        dwidth: change in width (can be negative).
        dheight: change in height (can be negative).
        """
        self.width += dwidth
        self.height += dheight
        return(self.width, self.height)



blank = Point(3,4)
print('blank', blank.get())

box = Rectangle(100, 200, blank)
print(box.get())

center = box.find_center()
print('center', center.get())

print(box.width)
print(box.height)

print('grow')
box.grow_rectangle(50, 100)
print(box.width)
print(box.height)
