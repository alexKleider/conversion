# File c2f.py

"""
User is prompted to enter a Celsius value
and gets the Fahrenheit value in return.
"""

from ck_input import ck_input_digits_only, ck_input_float

def celsius_to_fahrenheit(celsius):
    """Takes a digits only string and
    returns a Fahrenheit value."""
    return float(celsius) * 9 / 5 + 32



if __name__ == "__main__":
    user_input = 'something'
    while user_input:
        user_input = input("Celsius: ")
        checked = ck_input_float(user_input)
        if checked:
            fahrenheit = celsius_to_fahrenheit(checked)
            print(f"{checked}C => {fahrenheit:4.2f}F")
        else:
            print(f"'{user_input}' isn't valid input!")
