#!/usr/bin/python3
""" Define a locked class"""
class LockedClass:
    """
    Only allows instansiation of the first_name arttribut
    """
    __slots__ = ["first_name"]
