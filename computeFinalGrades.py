import numpy as np
from roundGrade import roundGrade

grades = np.array([[4, 4, 4, 7], [7, 10, 12, 10], [2, 0, -3, 4]])
#grades = np.array([[4],[7],[12]])

def computeFinalGrades(grades):
    
    M = len(grades[0,:])
    
    gradesFinal = np.array([])
    
    if M == 1:
        for i in range(len(grades[:,0])):
            gradesFinal = np.append(gradesFinal, grades[i,0])
            
    if M > 1:
        for j in range(len(grades[:,0])):
             np.amin(grades[j,:])
    
    
    return gradesFinal

print(computeFinalGrades(grades))