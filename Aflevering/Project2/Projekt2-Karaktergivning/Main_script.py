"""
Welcome to our main script. 
You can run our program from here.

The whole assignment has been worked out by the whole group in collaboration,
but it has been divided into sections, each with a responsible group member.

RESPONSIBLE: Freja Terp Petersen, s184321.

"""

#   Importing libraries and functions. 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread("dtu.jpg")

import numpy as np
import os
import pandas as pd
from displayMenu import displayMenu
from dataCheck import dataCheck
from gradesPlot import gradesPlot
from dataToGrades import dataToGrades
from generateListGrades import generateListGrades

#   Defining items for the displayMenu function (used later).
menuItems = np.array(["Load new data", "Check for data errors", "Generate plots", "Display list of grades", "Quit"])
correctErrors = np.array(["Yes", "No"])

#   Defining variables
gradeScale = np.array([-3,0,2,4,7,10,12])

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
                #   We return the number of errors found in the dataCheck function.
                errs = dataCheck(data)
                
                #   If one or more errors occur...
                if errs != 0:
                    
                    #... we prompt the user, and ask if they want to correct the errors.
                    print("\nDo you wish to correct the errors on the grades?")
                    yesno = displayMenu(correctErrors)
                    
                    #   If they dont want to correct the errors, we print a 
                    #   service message, and the return to the main menu.
                    if yesno == 2:
                        print("You have choosen to not correct the errors. Be aware that this might influence the final grades of some pupils.\n")
                    
                    #   If the user want to correct the errors...
                    if yesno == 1:
                        
                        #... we iterate over the number of columns and rows. 
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
                                            
                                            #   If the input is not a valid number
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
                        
                        #   When loop is done, user is informed.                         
                        print("\nAll of the invalid grades have been viewed and corrected if you wished to.\n")                
                                                 
 #-----------------------------------------------------------------------------              
#Choise 3           
#RESPONSIBLE: Anna Sophie Bjerremand Jensen, s174349.
 
            #If the user chooses the the 3rd  main menuoption, it starts the while loop to show the plots
            if choice == 3:
                while True:

                    #Calls the gradesPlot function that show the two diagrams:"Final Grades" and "Grades per assignment" 
                    gradesPlot(grades)
                   
                    # Break to main menu
                    break
            
            # 4th choise of the main menu
            if choice == 4:
                while True:
                
                    # Show the list containing the student names, student IDs, the grades for each assignment as well as the final grades
                    print(generateListGrades(dfdata, grades))
                    print("\nSee list of grades above.\n")
                    
                    # We construct a for-loop to check for invalid grades.
                    ingradescale = np.array([[np.any(i == gradeScale)]for i in np.reshape(grades, np.size(grades))])
                    
                    # If one or more invalid grades are present, we print a 
                    # service message.
                    if np.any(ingradescale == False):
                        print("Note that there are one or more invalid grades in the data set.")
                        print("This may affect the final grades column.\n")

                    break
                    
            #The 5th choice of the main menu breaks/quits the program
            if choice == 5:
                plt.xticks([])
                plt.yticks([])
                imgplot = plt.imshow(img)
       
                #Breaks the main while-loop
                break
            
        #Break that quits the program   
        break

