# File: temperature_conversion.py

import re
import unittest

re_template = r"^(?P<value>[+-]?\d+(\.\d*)?)(?P<units>({}|{}))$"
temperature_re = re_template.format('C', 'F')
print(re_template)
print(temperature_re)
#temperature_re = r"^(?P<value>[+-]?\d+(\.\d*)?)(?P<units>(C|F))$"
temperature_pattern = re.compile(temperature_re, re.IGNORECASE)

flip_temp = str.maketrans("cCfF", "fFcC")

def c2f(c):
    return float(c) * 9 / 5 + 32

def f2c(f):
    return (float(f) - 32) * 5 / 9

def convert_temp(temperature):
    """
    Accepts a temperature reading in either Celsius or Fahrenheit.
    Input format must be a float followed by either C or F.
    If incorrect format, prints a complaint and returns None.
    If successful: returns a tuple(temp, F|C)
    """
    match = temperature_pattern.match(temperature)
    if match:
        value, units  = match.group("value", "units")
        flipped = units.translate(flip_temp) 
        
        if units.upper() == 'C':
            return (c2f(value), flipped)
        else: 
            return (f2c(value), flipped)

def initial_user_run_test():
    user_input = 'something'
    while user_input:
        user_input = input("Enter a temp: ")
        checked = convert_temp(user_input)
        if checked:
            print(f"Good: {checked[0]:.2f}{checked[1]}")
        else:
            print(f"'{user_input}' isn't a temperature!")

class TemperatureConversionTest(unittest.TestCase):

    testvalues = (
        ("-20.6C", "-5.08F"),
        ("-5.08F", "-20.60C"),
        ("-20.6c", "-5.08f"),
        ("-5.08f", "-20.60c"),
        ("60f", "15.56c"),
        ("15.56c", "60.01f"),
    )

    def test_temperature_conversion(self):
        for source, output in self.testvalues:
            with self.subTest(source=source, output=output):
                res = convert_temp(source)
                if res:
                    res = f"{res[0]:.2f}{res[1]}"
                self.assertEqual(res, output)


if __name__ == "__main__":
    initial_user_run_test()
#   unittest.main()

