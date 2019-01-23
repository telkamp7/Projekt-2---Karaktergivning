"""

    Function:       computeFinalGrades: Takes in a Numpy array and compute the
                    final grades.
                    For each student, the final grade must be computed in the 
                    following way:
                        -   If there is only one assignment (M = 1) the final grade
                            is equal to the grade of that assignment
                        -   If there are two or more assignments (M > 1) the lowest
                            grade is discarded. The final grade is computed as the
                            mean og M - 1 highest grades rounded to the nearest
                            grade on the scale (using the function roundGrade).
                        -   Irrespective of the above, if a student has receiced 
                            the grade -3 in one or more assignments, the final grade
                            must always be -3.
    
    Input:          A N x M numpy array containing grades given to N student for
                    M assignments.
        
    Output:         A numpy array containing the final grades given to N students.
    
    Respomsible: Kasper Telkamp Nielsen, s170397
    
"""

import numpy as np
from roundGrade import roundGrade

def computeFinalGrades(grades):
    
    #   We evaluate the number of assignments  
    M = len(grades[0,:])
    
    #   We construct an empty array
    gradesFinal = np.array([])
    
    #   If theres is one assignment, the gradesFinal is equal to grades.
    if M == 1:
        for i in range(len(grades)):
            gradesFinal = np.append(gradesFinal, grades[i,0]).astype(int)
            
    #   If there is more than one assignment, the gradesFinal is equal to
    #   the mean value of the grades (minus the minimum grade) rounded with
    #   the roundGrade function.
    if M > 1:
        
        for j in range(len(grades)):
            if np.any(grades[j,:] == -3):
                grades[j,:] = -3
        
        #   We calculate the mean values.
        studentMean = np.array([])        
        for i in range(len(grades)):
            minval = np.min(grades[i,:])
            studentMean = np.append(studentMean, (np.sum(grades[i,:]) - minval) / (M - 1))
            
        #   We calculate the final grade for each student using the roundGrade function.
        gradesFinal = roundGrade(studentMean)
    
    return(gradesFinal)
    
