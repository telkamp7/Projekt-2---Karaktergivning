import numpy as np
import pandas as pd

from dataLoad import *


def dataCheck(data):
    
    #   Define the column with student IDs as vector.
    studentID = data[:,0]
    
    #   Find and count the unique studentIDs and put them into vectors.
    unique, uniquecnt = np.unique(studentID, return_counts = True)
    #   Fill the vector 'notunique' with the studentIDs from 'unique-vector' 
    #   which appear twice according to the 'uniquecnt'-vector.
    notunique = unique[uniquecnt > 1]
    
    #   Fill the list 'err' with information on the not unique student IDs.
    err = pd.DataFrame([data[studentID == i] for i in notunique])
    
    #   Print errormessages. 
    if len(notunique)>0:
        print("The following student ID(s) were found to be duplicates: {}".format(notunique))
        print("We found the following information on the student ID(s): \n{}".format(err),sep = "\n")
    else: 
        print("We found no errors in the list of student IDs.")


    #Define a vector with the grading scale:
    gradeScale = np.array([-3,0,2,4,7,10,12])
    
    grades = np.array(datagrade)
    
    #Define length of matrix containing all the grades 
    n = len(grades)
                    
    #Create a for-loop that checks if the grade givin is contained in the grading scale:
    for i in range(n):
        #Only checks the columns that contains grades (numcol-2)
        for j in range((numcol-2)):
            #If the grade is within the Scale, inserts a true
            if np.any(grades[i,j] == gradeScale):
                grades[i,j] = True
                print("We found no errors in the given grades.")
                
            #If the grade is not within the scale, inserts false.
            else:
                grades[i,j] = False
               
                #Prints the name and student ID of the student that has an incorect grade according to the grading scale
                #plus the assignment in which the mistake occurs. 
                print("{:s}, {:s} has an incorect grade in assignment {}.".format(data[i,1],data[i,0],j+1))