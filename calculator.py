"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# No setup
# repeat forever:
while True:
#     read input
    user_input = raw_input("> ")
#     tokenize input
    tokens = user_input.split(" ")

#     if the first token is "q":
    if tokens[0] == "q":
#         quit
        break

#     else:
#         decide which math function to call based on first token
    else:

        #  for the other tokens in the list, convert strings to floats
        for i in range(len(tokens)):
            if i > 0:
                tokens[i] = float(tokens[i])

        # checks for add sign, then calls add function
        if tokens[0] == "+":
            print add(tokens[1], tokens[2])
