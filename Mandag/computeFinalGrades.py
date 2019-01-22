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
        
        #Calculate mean values.
        studentMean = np.array([])        
        for i in range(len(grades)):
            minval = np.min(grades[i,:])
            studentMean = np.append(studentMean, (np.sum(grades[i,:]) - minval) / (M - 1))
            
        #   We calculate the final grade for each student using the roundGrade function.
        gradesFinal = roundGrade(studentMean)
    
    return(gradesFinal)
    
