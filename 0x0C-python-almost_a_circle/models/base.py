#!/usr/bin/python3
"""
define a Base class
"""

class Base:
    """ initialize class Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Construct a Base instance.

        Args:
            id (int, optional): unique identifier for the instance, defaults to None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

