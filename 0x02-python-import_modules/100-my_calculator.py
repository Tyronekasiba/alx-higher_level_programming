#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ ==  "__main__":
    item = argv[1:]
    operator = ["+", "-", "*", "/"]
    count = len(item)
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")

    else:
        if argv[2] == operator[0]:
            a = int(item[0])
            b = int(item[2])

            print("{} + {} = {}".format(a, b, add(a,b)))



        elif argv[2] == operator[1]:
            a = int(item[0])
            b = int(item[2])

            print("{} - {} = {}".format(a, b, sub(a,b)))



        elif argv[2] == operator[2]:
            a = int(item[0])
            b = int(item[2])

            print("{} * {} = {}".format(a, b, mul(a,b)))


        else:
            argv[2] == operator[3]
            a = int(item[0])
            b = int(item[2])

            print("{} / {} = {}".format(a, b, div(a,b)))

