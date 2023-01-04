#!/usr/bin/python3
""" A class of a Rectangle """


class Rectangle:
    """a class containing height and width methods"""
    def __init__(self, width=0, height=0):
        """initiating width and height attributes of the class
            width and height have a default value of 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """a property method that gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ a method that sets up the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a property method that gets the value of height"""
        return self._height

    @width.setter
    def height(self, value):
        """ a method that sets up the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
