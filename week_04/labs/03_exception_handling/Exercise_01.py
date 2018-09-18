'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

import time

class NotAnInt(Exception):

    """Exception handling if integer expected

    Attributes:
        message (str): Description
    """

    def __init__(self):
        self.message = "Not an integer"

print(chr(27) + "[2J")
print("Method 1")
time.sleep(1)
print(chr(27) + "[2J")

while True:

    try:
        _input = int(input("Please enter an integer: "))
        print(_input, "is an integer")
        break

    except ValueError as ve:
        print("Error:", ve, "\nnot an integer - try again")
        continue

print(chr(27) + "[2J")
print("Method 2")
time.sleep(1)
print(chr(27) + "[2J")


while True:

    # Take user input and make a list out of all the characters
    _input_raw = input("Please enter an integer: ")
    _input = list(_input_raw)

    # Check if each letter is a digit. If not, the user has not entered an integer and is told so and asked to try again
    try:
        for letter in _input:
            if letter.isdigit() == False:
                raise NotAnInt()
        break
    except NotAnInt as ni:
        print("Error:", ni.message, "- try again")
        continue

# Reassemble and print
print("your number is", "".join(_input))

# Or better yet - just use the raw input
print("your number is", _input_raw)
