# Import libraries

import numpy as np
import os
from displayMenu import *
from dataLoad import dataLoad
from dataCheck import dataCheck
from gradesPlot import gradesPlot
from dataToGrades import dataToGrades
from generateListGrades import generateListGrades

# Define menu items
menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit"])


# Define empty name variable
# Start
# ------------------------------------------------------------------
#Load in data
while True:
    
    print("Enter the filename of a CSV-file or enter 0 to quit the program.")
    filename = input("Please enter filename: ")
    
    if filename == "0":
        #   Quit the program
        break
       
    if not  filename.endswith(".csv") or not os.path.isfile(filename):
        print("Du lugter")
        continue
    
    elif  filename.endswith(".csv") and os.path.isfile(filename):
        
        #   Load in data
        data = dataLoad(filename)
        data = np.array(data)
        grades = dataToGrades(data)
        
        #   Service message
        print("\nThe data, {}, has been succesfully loaded.".format(filename))
        print("There is a total number of {} students in the loaded data, and the number of graded assignments is {}.\n".format(len(data), len(data[0,:])-2))
        
        while True:
            choice = displayMenu(menuItems)
            
            if choice == 1:
                while True:
                    print("Enter the filename of a CSV-file or enter 0 to exit to the main menu.")
                    filename = input("Please enter filename: ")
        
                    if filename == "0":
                        #Break to main menu
                        break
        
                    elif  filename.endswith(".csv") and os.path.isfile(filename): 
                        
                        #   Service message
                        print("\nThe data, {}, has been succesfully loaded.".format(filename))
                        
                        #   Load in data
                        data = dataLoad(filename)
                        data = np.array(data)
                        grades = dataToGrades(data)
                        
                        #   Break to main menu
                        break
                
                    else:
                        print("\nDU ER DUM\n")
                
            if choice == 2:
                dataCheck(data)
                
            if choice == 3:
                while True:
                    #   Checks if there is any data left in the data set.
                    if np.size(data) == 0:
                    #   Prints an error message if data is empty
                        print("There is no data left in your data-set")
                    
                        #   Break to main menu
                        break
              
                    else:
                        #   Show the diagrams
                        gradesPlot(grades)
                        #   Prints a service message
                        print("Your diagrams has been succesfully shown")
                        #   Break to main menu
                        break
            
            
            if choice == 4:
                while True:
                 #   Checks if there is any data left in the data set.
                    if np.size(data) == 0:
                    #   Prints an error message if data is empty
                        print("There is no data left in your data-set")
                    
                        #   Break to main menu
                        break
                    
                    else:
                        #   Show the list of grades with student names and final grades
                        print(generateListGrades(filename, grades))
                        print("\n")
                        
                        break
                
            
            if choice == 5:
                break
        
    #   Quit the program   
    break
