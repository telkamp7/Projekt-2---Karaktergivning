  """
Dette script er lånt fra undervisningsmaterialet 'modules_python.pdf' 
side 64 men indeholder betydelige ændringer.

The whole assignment has been worked out by the whole group in collaboration,
but it has been divided into sections, each with a responsible group member.
   
RESPONSIBLE: Anna Sophie Bjerremand Jensen, s174349.
"""

"""
DISPLAYMENU Displays a menu of options, ask the user to choose an item
and returns the number of the menu item chosen.

Usage: choice = displayMenu(options)

Input    options   Menu options (array of strings)
Output   choice    Chosen option (integer)

Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
"""
    
import numpy as np
from inputNumber import *

#

def displayMenu(options):
  
    
    # Display menu options
    for i in range(len(options)):
        #   Print a menu with the menu options. {:d}. - print the options number, i+1  {:s} - prints a string with options.
        print("{:d}. {:s}".format(i+1, options[i]))
    #   Set choice = 0 
    choice = 0
    #   If the input number is equal to one of the options numbers
    
    #This while loop has been crafted by the group. 
    while True:
        #Prompts the user for an input as a number from the main menu
        choice = inputNumber("Please, choose a number from the options: ")
        
        # if the input isn´t a valid number from the menuoptions, an error-message is printed, and the user is asked for a new input 
        if not np.any(choice == np.arange(len(options)+1)):
            print("\nAn error occurred. Make sure to input a number from the menu.")
            pass
        
        else:
            break
        
    return choice