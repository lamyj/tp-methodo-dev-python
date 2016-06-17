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
        "*": multiplication,
        "/": division,
    }

    if operator not in operations:
        raise Exception("Unknown operator: {}".format(operator))

    return operations[operator]

def parse_operand(value):
    """ Return the value contained in the operand, which must be a real number 
        or the value "pi".
    """

    if value == "pi":
        return 3.14
    else:
        return float(value)

def addition(left, right):
    """Parse left and right as numbers, return a string containing their sum."""

    return str(parse_operand(left)+parse_operand(right))

def subtraction(left, right):
    """Parse left and right as numbers, return a string containing their difference."""

    return str(parse_operand(left)-parse_operand(right))

def multiplication(left, right):
    """Parse left and right as numbers, return a string containing their product."""

    return str(parse_operand(left)*parse_operand(right))

def division(left, right):
    """ Parse left and right as numbers, return a string containing their quotient.
        If the right operand equals zero, NaN is returned.
    """

    result = None
    try:
        result = parse_operand(left)/parse_operand(right)
    except ZeroDivisionError as e:
        result = float("nan")
    return str(result)

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
