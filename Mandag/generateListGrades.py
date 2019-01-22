import numpy as np
import pandas as pd
from dataLoad import dataLoad
from computeFinalGrades import computeFinalGrades

def generateListGrades(filename, grades):
    
    finalGrades = computeFinalGrades(grades)
    
    #Import data with the dataLoad function.
    dfdata = dataLoad(filename)
    
    #Transforms finalGrades-vector to dataframe of type string.
    dffinalGrades = pd.DataFrame({'Final Grades':finalGrades}).astype(str)
    
    #Join together the two dataframes
    listGradesunsort = pd.concat([dfdata, dffinalGrades], axis = 1)
    
    #Using argsort to get index from sorted values. 
    index = listGradesunsort.Name.values.argsort()
    
    #Sorting, using the indices
    #https://stackoverflow.com/questions/43401903/python-order-dataframe-alphabetically
    listGrades = pd.DataFrame(listGradesunsort.values[index], listGradesunsort.index[index], listGradesunsort.columns)
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', -1)
    
    return(listGrades)
    



