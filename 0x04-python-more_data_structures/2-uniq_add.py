#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ 
    uniq_list = set()
    sum = 0
    for x in my_list:
        if x not in uniq_list:
            uniq_list.add(x)
        sum =+ x
    return sum
    """
    """
    Returns the sum of all unique integers in a list.
    """

    uniq_list = set()
    sum = 0
    for num in my_list:
        if num not in uniq_list:
            uniq_list.add(num)
            sum += num
    return sum
    
