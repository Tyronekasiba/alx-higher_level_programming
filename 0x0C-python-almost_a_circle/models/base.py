#!/usr/bin/python3
"""
Base class for all models
"""

class Base:
    __nb_objects = 0  # a private class attribute

    def __init__(self, id=None):
        """
        Construct a Base class.

        Args:
            id (int, optional): unique identifier for the instance, default to None
        """

        if id is not None:
            # if id is provided, assign to public instance attribute
            self.id = id
        else:
            # if id is not provided, increment nb_objects and assign to public
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

