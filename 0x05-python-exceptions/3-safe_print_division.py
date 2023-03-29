#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns division of a and b"""
    try:
       Div_result = a / b
    except(TypeError, ZeroDivisionError):
        Div_result = None
    finally:
        print("Inside result: {}".format(Div_result))
        return(Div_result)

