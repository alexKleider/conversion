# File: ck_input.py

import re

digits_only_re = r"^\d+$"
digits_only_pattern = re.compile(digits_only_re)

float_re = r"^[-+]?\d+([.]\d*)?$"
float_pattern = re.compile(float_re)

def ck_input_digits_only(input_string, use_regex = True):
    """Returns the <input_string> if it consists
    only of digits, otherwise returns None.
    Implemented using regex by default
    but could be implemented in a much simpler way
    using the string method isdigit.
    """
    if not use_regex:
        if input_string.isdigit():
            return input_string
    else:
        digits_only_match = digits_only_pattern.match(input_string)
        if digits_only_match:
            return digits_only_match.group()

def ck_input_float(input_string):
    float_match = float_pattern.match(input_string)
    if float_match:
        return float_match.group()

if __name__ == "__main__":
    user_input = 'something'
    while user_input:
        user_input = input("Digits only please: ")
        checked = ck_input_digits_only(user_input, False)
        if checked:
            print(f"Good: {checked}")
        else:
            print(f"'{user_input}' isn't all digits!")

