#!/usr/bin/python3
def safe_print_division(a, b):
    try:
       Div_result = a / b
    except(TypeError, ZeroDivisionError):
        print("Error: Division by Zero")
        return None
    else:
        return(Div_result)
    finally:
        print("Inside result: {}".format(Div_result))
        return(Div_result)

