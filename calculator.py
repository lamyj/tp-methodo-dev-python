#!/usr/bin/env python

from __future__ import print_function
import sys

def parse_operator(operator):
    """ Return the function associated with the given operator. 
        Raise an exception on unknown operators.
    """

    operations = {
        "+": addition,
        "-": subtraction,
        "*": multiplication
    }

    if operator not in operations:
        raise Exception("Unknown operator: {}".format(operator))

    return operations[operator]

def addition(left, right):
    """Parse left and right as numbers, return a string containing their sum."""

    return str(float(left)+float(right))

def subtraction(left, right):
    """Parse left and right as numbers, return a string containing their difference."""

    return str(float(left)-float(right))

def multiplication(left, right):
    """Parse left and right as numbers, return a string containing their product."""

    return str(float(left)*float(right))

def main():
    operator = raw_input("Operator: ")
    try:
        operation = parse_operator(operator)
    except Exception as e:
        print(e)
        return 1

    left = raw_input("Left operand: ")
    right = raw_input("Right operand: ")
    result = operation(left, right)
    print("Result:", result)

if __name__ == "__main__":
    sys.exit(main())
