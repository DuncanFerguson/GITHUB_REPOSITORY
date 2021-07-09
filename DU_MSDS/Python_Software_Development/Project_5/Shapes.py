# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Project 5: Shapes
# Date: 3/11/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

"""The area of all the shapes in this program can be found with the combination of the height and base. This is not
 to be confuse with length. The height of which the object obtains with a flat
base. Circles and squares have heights and bases that are equal to each other. The circle has height and base of
it's diameter. A square has base and height of it's sides. For this project we will find the area of the respective
shapes with their height's and bases."""

import math


class Shape(object):
    """A Shape Class that is the basis for the later classes. There are two different types of shapes. And Oval and a
    polygon. All other shapes are a subclass of those two. For general purposes, we are listing the area of a shape
    as the base times the height. Theses are over written by the proceeding shapes."""
    def __init__(self, area, name="Shape"):
        self.area = area
        self.name = name
        super(Shape, self).__init__()

    def __str__(self):
        return "A {} shape has an area of {}".format(self.name, self.area)

    def area(self):
        """Area function that is universal to all Shape"""
        return self.area()


class Polygon(Shape):
    """All Polygons are a type of Shape"""
    def __init__(self, area, name="Polygon"):
        self.area = area
        self.name = name
        super().__init__(self.area, self.name)


class Parallelogram(Polygon):
    """All Parallelograms are Polygons"""
    def __init__(self, area, name="Parallelogram"):
        self.name = name
        self.area = area
        super().__init__(self.area, self.name)


class Rectangle(Parallelogram):
    """A rectangles area is the height times base"""
    def __init__(self, height, base, name="Rectangle"):
        self.height = height
        self.base = base
        self.name = name
        self.area = self.area()
        super().__init__(self.area, self.name)

    def area(self):
        return self.base*self.height


class Square(Rectangle):
    """All Squares Are Rectangles and Rhombus"""
    def __init__(self, height, name="Square"):
        self.name = name
        self.height = height
        super().__init__(self.height, self.height, self.name)


class Rhombus(Parallelogram):
    """ A Rhombus is a special type of parallelogram, where all sides are equal. It can be a square but not a rectangle
    it is always a parallelogram. Don't be confused about the height base area computation with it being the same
    as the sides times each other. The base is the same as one side, but the height will vary upon the angles"""
    def __init__(self, base, height, name="Rhombus"):
        self.name = name
        self.base = base
        self.height = height
        super().__init__(self.area, self.name)

    def area(self):
        return self.base*self.height


class Oval(Shape):
    """All ovals are shapes are half the base times the half the height times pi. The base is the total horizontal
    length of the oval, while the height is the total vertical length of the oval by halving these measurements we
    get the two radius measurements needed to calculate the height"""
    def __init__(self, base, height, name="Oval"):
        self.name = name
        self.base = base
        self.height = height
        self.area = self.area()
        super().__init__(self.area, self.name)

    def area(self):
        return (self.base * self.height * math.pi)/2


class Circle(Oval):
    """The area of a Circle is the same of the area of an oval, but instead of having two radius measurements
    it has one. Note the Base is the same as the vertical or horizontal length measurement of the circle. Also known
    as the diameter."""
    def __init__(self, base, name="Circle"):
        self.name = name
        self.base = base
        super().__init__(self.base, self.base, self.name)


class Pentagon(Polygon):
    """The Area if a regular Pentagon can be found with only one side length. If this side is placed horizontal
    it is then the base."""
    def __init__(self, side, name="Pentagon"):
        self.side = side
        self.area = self.area()
        self.name = name
        super().__init__(self.area, self.name)

    def area(self):
        return self.side**2*.25*math.sqrt(5*(5+2*math.sqrt(5)))


class Triangle(Polygon):
    """The Area of a triangle can be found with the base times the height divided by 2"""
    def __init__(self, height, base, name="Triangle"):
        self.name = name
        self.height = height
        self.base = base
        self.area = self.area()
        super().__init__(self.area, self.name)

    def area(self):
        return (self.height * self.base) / 2


def shapes():
    """The Shapes that we are taking the length of all the shapes are the base and height. For all the polygons the
     base is the length of one side laid horizontally, while the height is the total vertical measurement of the object
     For ovals the base is the horizontal diameter, and the height it the vertical diameter"""
    h = 10
    b = 11

    print(Shape(b))  # Inputting b as an area
    print(Polygon(b))  # Inputting b as an area
    print(Parallelogram(b))  # Inputting b as an area
    print(Square(b))  # Using B as one of the lengths
    print(Rectangle(b, h))  # Using H and B as the sides
    print(Oval(h, b))  # Using H and B as the diameters
    print(Circle(h))  # Using H as the diameter
    print(Pentagon(b))  # Using B as the length of the side
    print(Triangle(h, b))  # Using H and B as the height of a triangle


def main():
    """The Real main function for starting the code is user_inputs. The start game function is meant for testing.txt."""
    shapes()


if __name__ == "__main__":
    main()
