#!/usr/bin/python3
""" define Area and Perimeter of a Rectangle"""
class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrive rectangle's with | setting with of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """ private instance with attribute """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """ Get rectangle's height | setting the height """ 
        return self._height

    @height.setter
    def height(self, value):
        """ Private instance height attribute """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value
    def area(self):
        """ Getting  area of the rectangle """
        return (self.width * self.height)
    def perimeter(self):
        """ perimeter of rectangle """
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = ((2 * self.width) + (2 * self.height))
        return perimeter

