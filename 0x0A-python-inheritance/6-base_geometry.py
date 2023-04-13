#!/usr/bin/python3
""" this module defines a base geometry class """


class BaseGeometry:
    """ represent a base geometry class """
    def area(self):
        """ raises exception not implemented """
        raise Exception("area() is not implemented")
