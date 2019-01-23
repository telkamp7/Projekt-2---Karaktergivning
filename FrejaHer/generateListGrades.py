"""
GENERATE LIST GRADES
The purpose of this function is to generate the full list of all student IDs,
names and grades including the final grade.

INPUT: dfdata: N x M dataframe of the loaded data with names in first column,
       student IDs in the second and grades in the remaining M-2 columns.
       grades: N x (M-2) dataframe of the grades.

OUTPUT: listGrades: list of all of the above + a column with the Final Grades.
    

The whole assignment has been worked out by the whole group in collaboration,
but it has been divided into sections, each with a responsible group member.

RESPONSIBLE: Freja Terp Petersen, s184321.

"""

#   We import the pandas package and the computeFinalGrades function.
import pandas as pd
from computeFinalGrades import computeFinalGrades

def generateListGrades(dfdata, grades):
    
    #   Defining the final grades as a vector using the computeFinalGrades 
    #   function.
    finalGrades = computeFinalGrades(grades)
    
    #   Transforming 'finalGrades'-vector into dataframe.
    dffinalGrades = pd.DataFrame({'Final Grades':finalGrades})
    
    #   Joining together the two dataframes by columns using the pd.concat 
    #   function. The dataframe hasn't been sorted alphabetically yet. 
    listGradesunsort = pd.concat([dfdata, dffinalGrades], axis = 1)
    
    #   Using np.argsort to get index from sorted values.
    #   Sorting by the 'Name' column. 
    index = listGradesunsort.Name.values.argsort()
    
    #   Sorting the dataframe, using the indices above
    #   documentation: https://stackoverflow.com/questions/43401903/python-order-dataframe-alphabetically
    listGrades = pd.DataFrame(listGradesunsort.values[index], listGradesunsort.index[index], listGradesunsort.columns)
    
    #   Setting options which allow the whole dataframe to be shown when printed.
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', -1)
    
    return(listGrades)
    



