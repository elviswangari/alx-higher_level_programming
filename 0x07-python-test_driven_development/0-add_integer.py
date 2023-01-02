#!/usr/bin/python3
"""

    This module contains one function that adds two integers

"""


def add_integer(a, b=98):
    """A function that add two integers

       Args:
           a: first argument
           b: second argument

       Returns:
           Sum of the two arguments

       Raises:
           TypeError: If either of the arguments not an integer or a float
    """

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif (not isinstance(b, int)) and (not isinstance(a, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
