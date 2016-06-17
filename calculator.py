#!/usr/bin/env python

from __future__ import print_function
import sys

def addition(left, right):
    """Parse left and right as numbers, return a string containing their sum."""

    return str(float(left)+float(right))

def main():
    left = raw_input("Left operand: ")
    right = raw_input("Right operand: ")
    result = addition(left, right)
    print("Result:", result)

if __name__ == "__main__":
    sys.exit(main())
