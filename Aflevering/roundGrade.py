"""
 Function:       roundGrades: Takes the mean vallue of all the greated assignments for each student (the final grade)
                 and rounds it to a valid great from the gradeScale
    
 Input:          A vector containing the finalgrade for each student in the loaded data
        
 Output:         A vector containing the rounded final grade for each student in the loaded data
    
 Respomsible: Anna Sophie Bjerremand Jensen, s174349.
"""
import numpy as np


def roundGrade(grades):
    
    #   We set up bins. If the value is between two bins, it is assigned an
    #   index number which is asociated with the index in gradeScale, that the
    #   value is supposed to be assigned to.
    bins = np.array([-5, -1.5, 1.5, 3, 5.5, 8.5, 11, 15])
    gradeScale = np.array([-3, 0, 2, 4, 7, 10, 12])
    gradesRounded = gradeScale[np.digitize(grades, bins) - 1]
    
    return gradesRounded