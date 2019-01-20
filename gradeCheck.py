import numpy as np
from dataLoad import *


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
            
        #If the grade is not within the scale, inserts false.
        else:
            grades[i,j] = False
           
            #Prints the name and student ID of the student that has an incorect grade according to the grading scale
            #plus the assignment in which the mistake occurs. 
            print("{:s}, {:s} has an incorect grade in assignment {}.".format(data.iloc[i,1],data.iloc[i,0],j+1))