#!/usr/bin/python3
""" this module contains a function that  returns True if the object is an insta    nce of a class that inherited (directly or indirectly) from the specified cl    ass ; otherwise False
"""


def inherits_from(obj, a_class):
    """ 
    returns True if the object is an insta    nce of a class that inherited (dir    ectly or indirectly) from the specified class ; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

