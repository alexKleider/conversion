# File: convert.py

"""
Provides Conversion:
a class that creates instances for
specific unit conversion capablility.

First instance created is for temperature:
from convert import tempCF
tempCF.convert(temp) => (value, units)
"""


import re
import unittest

re_template = r"^(?P<value>[+-]?\d+(\.\d*)?)(?P<units>({}|{}))$"

flip_temp = str.maketrans("cCfF", "fFcC")

def c2f(c):
    return float(c) * 9 / 5 + 32

def f2c(f):
    return (float(f) - 32) * 5 / 9

class Conversion(object):

    def __init__(self, pattern, u1, u2, flip, f1, f2):
        self.pattern = pattern
        self.u1 = u1
        self.u2 = u2
        self.flip = flip
        self.f1 = f1
        self.f2 = f2
    
    def convert(self, user_input):
        match = self.pattern.match(user_input)
        if match:
            value, units = match.group("value", "units")
            flipped = units.translate(self.flip)

            if units.upper() == self.u1:
                return (self.f1(value), flipped)
            elif units.upper() == self.u2:
                return (self.f2(value), flipped)
            else:
                print("Major ERROR!!!!")

tempCF = Conversion(
    re.compile(re_template.format('C', 'F'), re.IGNORECASE), 
    "C", "F", str.maketrans("cCfF", "fFcC"),
    lambda c: float(c) * 9 / 5 + 32,
    lambda f: (float(f) - 32) * 5 / 9
    )

def initial_user_run_test(conversion):
    user_input = 'something'
    while user_input:
        user_input = input("Enter a temp: ")
        checked = conversion.convert(user_input)
        if checked:
            print(f"Good: {checked[0]:.2f}{checked[1]}")
        else:
            print(f"'{user_input}' isn't valid!")


if __name__ == "__main__":
    initial_user_run_test(tempCF)
#   unittest.main()
