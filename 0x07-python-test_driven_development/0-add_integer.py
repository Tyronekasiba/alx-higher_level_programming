#!/usr/bin/python3
""" Define addition of integer in a function """
def add_integer(a, b=98):
    """ Returns addition of a and b integers
    float arguments must be typecasted to int before addition is done
    and raises a type error if the urgument is not a float or an iteger:

    raise:
    TypeError: if a or b is not either an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be a float")
    return (int(a) + int(b))
