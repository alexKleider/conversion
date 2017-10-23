# File: convert.py

"""
Provides Conversion:
a class that creates instances for
specific unit conversion capablility.

First instance created is for temperature:
from convert import tempCF
tempCF.convert(temp) => (value, units)
<temp> must be a string consisting of a string
representation of a float followed immediately
by the letter c or the letter f.  Case doesn't matter.

Next for distances (Kilometers/Miles)
from convert import distanceKmMi
distanceKmMi.convert(distance) => (value, units)
<distance> must be a string consisting of a string
representation of a float followed immediately
by the letter sequence 'Km' or 'Mi'. Case does matter.
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

    def __init__(self, u1, u2, flip, f1, f2):
        self.pattern = re.compile(
            re_template.format(u1, u2), re.IGNORECASE) 
        self.u1 = u1
        self.u2 = u2
        self.flip = flip
        self.f1 = f1  # u1 ==> u2
        self.f2 = f2  # u2 ==> u1
    
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
    "C", "F", str.maketrans("cCfF", "fFcC"),
    lambda c: float(c) * 9 / 5 + 32,
    lambda f: (float(f) - 32) * 5 / 9
    )

distanceKmMi = Conversion(
    "KM", "MI", str.maketrans("kKmMi",
                              "mMiKm"),
    lambda k: float(k) / 1.60934,
    lambda m: float(m) * 1.60934
    )

def initial_user_run_test(conversion, measure):
    user_input = 'something'
    while user_input:
        user_input = input("Enter a {}: ".format(measure))
        checked = conversion.convert(user_input)
        if checked:
            print(f"Good: {checked[0]:.2f}{checked[1]}")
        else:
            print(f"'{user_input}' isn't valid!")


if __name__ == "__main__":
    initial_user_run_test(distanceKmMi, 'distance')
#   initial_user_run_test(tempCF, 'temperature')
#   unittest.main()
