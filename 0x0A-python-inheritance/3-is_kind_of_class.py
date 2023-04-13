#!/usr/bin/python3
"""
this module contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance inherited from a_class,
    otherwise False
    """
    return (isinstance(obj, a_class))
