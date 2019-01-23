

#RESPONSIBLE: Freja Terp Petersen, s184321.

# Import libraries

import numpy as np
import os
import pandas as pd
from displayMenu import *
from dataCheck import dataCheck
from gradesPlot import gradesPlot
from dataToGrades import dataToGrades
from generateListGrades import generateListGrades

# Define menu items
menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit"])
correctErrors = np.array(["Yes", "No"])


# Define empty name variable
# Start
# ------------------------------------------------------------------
#Load in data
while True:
    
    print("Velkomst")
    
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
        dfdata = pd.read_csv(filename)
        data = np.array(dfdata)
        grades = dataToGrades(data)
        
        #   Service message
        print("\nThe data, {}, has been succesfully loaded.".format(filename))
        print("There is a total number of {} students in the loaded data, and the number of graded assignments is {}.\n".format(len(data), len(data[0,:])-2))
       
        while True:
            choice = displayMenu(menuItems)
 
#-----------------------------------------------------------------------------           
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
                        dfdata = pd.read_csv(filename)
                        data = np.array(dfdata)
                        grades = dataToGrades(data)
                        
                        #   Break to main menu
                        break
                
                    else:
                        print("\nDU ER DUM\n")

#-----------------------------------------------------------------------------
### RESPONSIBLE: Kasper Telkamp Nielsen, s170397.              
            if choice == 2:
                #   We return the number of errors found in the dataCheck function.
                errs = dataCheck(data)
                
                #   If more than one error occured...
                if errs != 0:
                    
                    #... we prompt the user, and ask if they want to correct the errors.
                    print("\nDo you wish to correct the errors on the grades?")
                    yesno = displayMenu(correctErrors)
                    
                    #   If they dont want to correct the errors, we print a 
                    #   service message, and the return to the main menu.
                    if yesno == 2:
                        print("You have choosen to not correct the errors. Be aware that this might influence the final grades of some pupils.")
                    
                    #   If the do want to correct the errors...
                    if yesno == 1:
                        
                        #... we define the gradeScale...
                        gradeScale = np.array([-3,0,2,4,7,10,12])
                        #...and we iterate over the number of columns and rows. 
                        for i in range(len(grades)):
                            for j in range(len(grades[0,:])):
                                #   If a grade given to a student does not match a
                                #   possible grade on the gradeScale, we print a service
                                #   message to inform the user about which student, and
                                #   in which assignment the error occured.
                                if not np.any(grades[i,j] == gradeScale):
                                    print(data[i,:])
                                    print("There is an invalid grade in assignment {} in the row above.".format(j+1))
                                    
                                    #   Now we prompt the user to enter a valid grade from 
                                    #   the gradeScale. We update the grade in all
                                    #   the variables that it is needed. If the user
                                    #   want to skip correcting the invalid grade of
                                    #   a student the user can press 1.
                                    while True:
                                        try:
                                            newgrade = float(input("Please enter a valid grade or enter 1 to skip: "))
                                            
                                            #   If the input is a valid number on the gradeScale
                                            if np.any(newgrade == gradeScale):
                                                grades[i,j] = newgrade
                                                data[i,j+2] = newgrade
                                                dfdata.iloc[i,j+2] = newgrade
                                                #   We break out to the for-loop. 
                                                #   If there are no more errors,
                                                #   we break out to the main menu.
                                                break
                                            
                                            #   If the input is one
                                            if newgrade == 1:
                                                print("You have skipped one grade")
                                                #   We break out to the for-loop. 
                                                #   If there are no more errors,
                                                #   we break out to the main menu.
                                                break
                                            
                                            #   If the input i neither a valid number
                                            #   on the gradeScale or one.
                                            else:
                                                print("Invalid input. Your input should be a number from the grade scale:")
                                                print(gradeScale)
                                                pass
                                            
                                        #   If the input is not a number.
                                        except ValueError:
                                            print("Invalid input. Your input should be a number from the grade scale:")
                                            print(gradeScale)
                                            pass
                                                 
 #-----------------------------------------------------------------------------              
#RESPONSIBLE: Anna Sophie Bjerremand Jensen, s174349.
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
                        print("Text me please.")
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
                        print(generateListGrades(dfdata, grades))
                        print("\n")
                        
                        break
                    
                
            if choice == 5:
                break
            
        #   Quit the program   
        break
