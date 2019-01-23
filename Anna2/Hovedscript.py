

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
                
                errs = dataCheck(data)
                
                if errs != 0:
                
                    print("\nDo you wish to correct the errors on the grades?")
                    yesno = displayMenu(correctErrors)
                
                    if yesno == 2:
                        print("jiknf")
                
                    if yesno == 1:
                        
                        gradeScale = np.array([-3,0,2,4,7,10,12])
                        for i in range(len(grades)):
                            for j in range(len(grades[0,:])):
                                if not np.any(grades[i,j] == gradeScale):
                                    print(data[i,:])
                                    print("There is an invalid grade in assignment {} in the row above.".format(j+1))
                                    while True:
                                        try:
                                            newgrade = float(input("Please enter a valid grade or enter 1 to skip: "))
                                            if np.any(newgrade == gradeScale):
                                                grades[i,j] = newgrade
                                                data[i,j+2] = newgrade
                                                dfdata.iloc[i,j+2] = newgrade
                                                break
                                            if newgrade == 1:
                                                print("You have skipped one grade")
                                                break
                                            
                                            else:
                                                print("Invalid input. Your input should be a number from the grade scale:")
                                                print(gradeScale)
                                                pass

                                        except ValueError:
                                            print("Invalid input. Your input should be a number from the grade scale:")
                                            print(gradeScale)
                                            pass
                                                 
#-----------------------------------------------------------------------------   
#Choise 3           
#RESPONSIBLE: Anna Sophie Bjerremand Jensen, s174349.
 
            #If the user chooses the the 3  main menuoption, it starts the while loop to show the plots
            if choice == 3:
                while True:
                    #   Checks if there is any data in the data set.
                    if np.size(data) == 0:
                    #   Prints an error message if data is empty
                        print("There is no data left in your data-set")
                    
                        #Break to main menu
                        break
              
                    else:
                        #Calls the gradesPlot function that show the two diagrams:"Final Grades" and "Grades per assignment" 
                        gradesPlot(grades)
                        #   Prints a service message
                        print("Above you can see 2 diagrams. The first plot is a histogram that shows the final grades and the number of students who got it.\nThe second diagram is a plot that shows the grade as well as the meangrade for each assignment.")
                        # Break to main menu
                        break
            
            # 4th choise of the main menu
            if choice == 4:
                while True:
                 #   Checks if there is any data in the data set.
                    if np.size(data) == 0:
                    #   Prints an error message if data is empty
                        print("There is no data left in your data-set")
                        #Break to main menu
                        break
                    
                    else:
                        # Show the list containing the student names, student IDs, the grades for each assignment as well as the final grades
                        print(generateListGrades(dfdata, grades))
                        print("\n")
                        
                        break
                    
            #The 5th choice of the main menu breaks/quits the program
            if choice == 5:
                #Breaks the main while-loop
                break
            
        #Break that quits the program   
        break
