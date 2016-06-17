#!/usr/bin/env python

from __future__ import print_function
import math
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
        "cos": cos,
        "sin": sin,
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

def parse_operands(operation):
    """Read the number of operands corresponding to operation."""

    counts = {
        addition: 2,
        subtraction: 2,
        multiplication: 2,
        division: 2,
        cos: 1,
        sin: 1,
    }

    if operation not in counts:
        raise Exception("Unknown operator: {}".format(operation))

    operands = []
    for i in range(counts[operation]):
        value = raw_input("Operand {}: ".format(1+i))
        operands.append(value)
    return operands

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

def cos(angle):
    """ Parse angle as a number and return a string containing the cosine of
        the value in radians.
    """

    return str(math.cos(parse_operand(angle)))

def sin(angle):
    """ Parse angle as a number and return a string containing the sine of
        the value in radians.
    """

    return str(math.sin(parse_operand(angle)))

def main():
    operator = raw_input("Operator: ")
    try:
        operation = parse_operator(operator)
    except Exception as e:
        print(e)
        return 1

    operands = parse_operands(operation)
    result = operation(*operands)
    print("Result:", result)

if __name__ == "__main__":
    sys.exit(main())
