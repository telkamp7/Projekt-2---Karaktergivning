import numpy as np
from roundGrade import roundGrade

#   Tests
grades = np.array([[4, 0, 4, 7], [7, -3, 12, 10], [2, 0, -3, 4]])
#grades = np.array([[4],[7],[12]])

def computeFinalGrades(grades):
    
    #   We evaluate the number of assignments  
    M = len(grades[0,:])
    
    #   We construct an empty array
    gradesFinal = np.array([])
    
    #   If theres is one assignment, the gradesFinal is equal to grades.
    if M == 1:
        for i in range(len(grades[:,0])):
            gradesFinal = np.append(gradesFinal, grades[i,0]).astype(int)
            
    #   If there is more than one assignment, the gradesFinal is equal to
    #   the mean value of the grades, minus the minimum grade, rounded with
    #   the roundGrade function.
    if M > 1:
        
        for j in range(len(grades[:,0])):
            if np.any(grades[j,:] == -3):
                grades[j,:] = -3
                    
        
        
        #   We create a mask to remove the minimum grade for each student.
        rem_minimum_grades = np.ma.masked_where(grades == np.resize(grades.min(axis = 1),[grades.shape[0],1]), grades)
        
        #   We calculate the mean grade, minus the minimum grade, for each student.
        studentMean = np.ma.mean(rem_minimum_grades, axis = 1)
        
        #   If a student receives -3 in atleast one assignement, the gradesFinal
        #   must return -3
        for m in range(len(grades[:,0])):
            if grades[m,0] == -3:
                studentMean[m] = -3
        
        #   We calculate the final grade for each student using the roundGrade function.
        gradesFinal = roundGrade(studentMean)
    
    return(gradesFinal)
    
print(computeFinalGrades(grades))
