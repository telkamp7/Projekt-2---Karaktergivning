"""

This script is inspired of the educational material 'modules_python.pdf'
page 62. It contains some changes.

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015

"""
"""
The whole assignment has been worked out by the whole group in collaboration,
but is has been divided into sections, each with a responsible group member.

RESPONSIBLE: Kasper Telkamp Nielsen, s170397.

"""


"""
inputNumber promps the user to input a number and outputs this, if the input a valid.

inputNumber display a message and waits for the user to input a number.
The user can only input a number and the while-loop continues if the user
input something else (read: letter).

"""
    
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("\nAn error occured. Make sure to input a number from the menu.")
            pass
    return num