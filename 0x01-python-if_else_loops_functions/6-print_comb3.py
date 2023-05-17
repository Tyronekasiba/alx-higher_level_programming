#!/usr/bin/python3
for j in range(0, 10):
    for x in range(1, 10):
        if j >= x:
            continue
        elif j == 8 and x == 9:
            print("{}{}".format(j, x))
        else:
            print("{}{}".format(j, x), end=", ")
