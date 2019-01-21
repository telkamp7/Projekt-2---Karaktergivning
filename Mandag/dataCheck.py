import numpy as np
import pandas as pd

from dataLoad import *
from dataToGrades import dataToGrades


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
        print("We found the following information on the student ID(s): \n{}\n".format(err),sep = "\n")
        


    #Define a vector with the grading scale:
    gradeScale = np.array([-3,0,2,4,7,10,12])
     
    #We call the function to convert the data into only grades.
    grades = dataToGrades(data)
    
    #Define length of matrix containing all the grades 
    n = len(grades)
    
    errs = 0
    #Create a for-loop that checks if the grade givin is contained in the grading scale:
    for i in range(n):
        #Only checks the columns that contains grades (numcol-2)
        for j in range(len(grades[0,:])):
            #If the grade is within the Scale, inserts a true

            if not np.any(grades[i,j] == gradeScale):
                #Prints the name and student ID of the student that has an incorect grade according to the grading scale
                #plus the assignment in which the mistake occurs. 
                print("{:s}, {:s} has an incorrect grade in assignment {}.".format(data[i,1],data[i,0],j+1))
                errs += 1
    
    if errs == 0 and np.size(notunique) == 0:
        print("\nWe found no errors in neither the student IDs nor the grades of the loaded data.\n")
    
    
    print("")
                