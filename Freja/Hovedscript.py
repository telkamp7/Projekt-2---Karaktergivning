"""
Welcome to our main script. 
You can run our program from here.

The whole assignment has been worked out by the whole group in collaboration,
but it has been divided into sections, each with a responsible group member.

RESPONSIBLE: Freja Terp Petersen, s184321.

"""

#   Importing libraries and functions. 
import numpy as np
import os
import pandas as pd
from displayMenu import *
from dataCheck import dataCheck
from gradesPlot import gradesPlot
from dataToGrades import dataToGrades
from generateListGrades import generateListGrades

#   Defining items for the displayMenu function (used later).
menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit"])
correctErrors = np.array(["Yes", "No"])


#   Start
# ------------------------------------------------------------------
#   1st step: Load in data

    #   Welcome message
print("\n*****")
print("Hello and welcome to our program.")
print("This program serves as a help for you to gain an overview of a great set of data on assignment grades belonging to a number of students.")
print("The program has been worked out by Kasper Telkamp Nielsen, Anna Sophie Bjerremand Jensen and Freja Terp Petersen. Enjoy.")
print("*****\n")
print("First, you must input the data that you wish to overview.")

while True:
    #   Asking for input.
    print("Enter the filename of a CSV-file or enter 0 to quit the program.")
    filename = input("Please enter filename: ")
    
    #   If the user enters '0' the program stops.
    if filename == "0":
        #   Quit the program
        break
    
    #   Testing if the input is a 'csv'-file and if it exists. 
    #   If not, the user has to try again.
    if not  filename.endswith(".csv") or not os.path.isfile(filename):
        print("\nERROR: The inputted file is not a 'csv'-file or is not available in your current working directory. Please, try again.\n")
        continue
    
    #   If the input exists and is a 'csv'-file the data will be loaded in and
    #   the program starts.
    elif  filename.endswith(".csv") and os.path.isfile(filename):
        
        #   Load in data (saving data as pd.dataframe).
        dfdata = pd.read_csv(filename)
        #   Saving data as a np.array as well.
        data = np.array(dfdata)
        #   Generating a 'grades'-vector using the dataToGrades function.
        grades = dataToGrades(data)
        
        #   Service message
        print("\nThe data, {}, has been succesfully loaded.".format(filename))
        print("There is a total number of {} students in the loaded data, and the number of graded assignments is {}.\n".format(len(data), len(data[0,:])-2))
       
        while True:
            choice = displayMenu(menuItems)
 
#-----------------------------------------------------------------------------           
#   Choice 1: Load new data
            if choice == 1:
                #   If the user chooses to load new data the program enters a 
                #   while loop with the same functions as above.
                while True:
                    #   Printing service messages and asking for new input.
                    print("\nYou have chosen to load new data.")
                    print("Enter the filename of a CSV-file or enter 0 to return to the main menu.")
                    filename = input("Please enter filename: ")
                    
                    #   If the user enters 0, he/she will be guided back to 
                    #   the main menu.
                    if filename == "0":
                        #Break to main menu
                        break
                    
                    #   If the user enters an input, the program checks for the
                    #   same errors as with the first input.
                    #   Does the file exist and is it a csv-file?
                    elif  filename.endswith(".csv") and os.path.isfile(filename): 
                        
                        #   Service message
                        print("\nThe data, {}, has been succesfully loaded.\n".format(filename))
                        
                        #   Load in data in the same way as above.
                        dfdata = pd.read_csv(filename)
                        #   Resetting the 'data'-vector and the 'grades' as well.
                        data = np.array(dfdata)
                        grades = dataToGrades(data)
                        #   Break to main menu
                        break
                    
                    #   If the file does not exist or is not a csv-file the
                    #   program prints an error message.
                    else:
                         print("\nERROR: The inputted file is not a 'csv'-file or is not available in your current working directory. Please, try again.")

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
                        #print("\nAll of the invalid grades have been viewed and corrected if you wished to.\n")                
                                                 
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
