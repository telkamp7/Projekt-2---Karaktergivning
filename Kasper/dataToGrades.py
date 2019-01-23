"""

    Function:       dataToGrades: Take in a data variable containing our data in a
                    numpy array. The function strips the numpy array from the 
                    first two columns containing studentID's and names. Thay way
                    only a numpy array containing the grades for the assignments is left
    
    Input:          A data set with the first two columns as strings (studentID's and names).
                    and the rest of the columns is grades given for M assignments.
        
    Output:         A numpy array containing the grades given to N students for M assignments.
    
    Respomsible: Kasper Telkamp Nielsen, s170397
    
"""

def dataToGrades(data):
    
    #   Counting number of columns
    numcol = len(data[0,:])
    
    #   Adding all of the grades to one dataframe
    grades = (data[:,2:numcol].astype(int)) 
    
    return grades