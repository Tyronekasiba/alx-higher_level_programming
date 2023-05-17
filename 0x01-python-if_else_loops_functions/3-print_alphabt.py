#!/usr/bin/python3
for var in range(ord('a'), ord('z') + 1):
    if chr(var) != 'q' and chr(var) != 'e':
        print("{}".format(chr(var)), end='')
