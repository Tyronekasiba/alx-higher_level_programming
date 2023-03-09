#!/usr/bin/python3
def fizzbuzz():
    # checking for the multiples of 3 and 5 and replcae with fizzbuzz
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("Fizzbuzz ", end="")
        elif x % 3 == 0:
            print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{}".format(x), end=" ")
