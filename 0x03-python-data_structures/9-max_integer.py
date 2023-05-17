#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_number = my_list[0]
    for x in range(1, len(my_list)):
        if max_number < my_list[x]:
            max_number = my_list[x]
        else:
            continue
    return max_number
