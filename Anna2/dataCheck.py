import numpy as np
import pandas as pd
from dataLoad import *
from dataToGrades import dataToGrades

#RESPONSIBLE: Anna Sophie Bjerremand Jensen, s174349.


def dataCheck(data):
    
    #Define the first column loaded data (csv-file) with student IDs as vector. 
    studentID = data[:,0]
    
    #Find and count the unique studentIDs and put them into vectors.
    unique, uniquecnt = np.unique(studentID, return_counts = True)
    #Fill the vector 'notunique' with the studentIDs from 'unique-vector' 
    #which appear twice according to the 'uniquecnt'-vector.
    notunique = unique[uniquecnt > 1]
    
    #Fill the list 'err' with information on the not unique student IDs.
    err = [data[studentID == i] for i in notunique]
    
    #check if there is a error in the studentnumbers of the loaded data, and adds the row to err. 
    if np.size(err) > 0:
        err = np.concatenate(err, axis=0 )
    
        #   Print errormessages. 
        if len(notunique)>0:
            print("The following student ID(s) were found to be duplicates: {}".format(notunique))
            print("We found the following information on the student ID(s): \n{}\n".format(err),sep = "\n")
        


    #Define a vector with the grading scale:
    gradeScale = np.array([-3,0,2,4,7,10,12])
     
    #We call the function dataToGrades to convertextract the grades from the loaded data.
    grades = dataToGrades(data)
    
    #Define the length of matrix containing all the grades which will be used in the for-loop
    n = len(grades)
    
    #Sets errs = 0 
    errs = 0
    
    #Create two for-loops that loops throug each element in the matrix containing the grades
    #and checks if the grade givin is a valid grade according to the grading scale:
    for i in range(n):
        for j in range(len(grades[0,:])):
            
            #If the grade is within the Scale - prints the name and student ID of the student that has an invalid grade according to the grading scale
                #plus the assignment in which the mistake occurs. 
            if not np.any(grades[i,j] == gradeScale):
                print("{:s}, {:s} has an invalid grade in assignment {}.".format(data[i,1],data[i,0],j+1))
                errs += 1
                
    #If the loaded data doesn´t have an error in neither the student Id nor the grades, prints a service message to the user.
    if errs == 0 and np.size(notunique) == 0:
        print("\nWe found no errors in neither the student IDs nor the grades of the loaded data.\n")

    return(errs)