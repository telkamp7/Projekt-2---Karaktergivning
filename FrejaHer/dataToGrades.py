#RESPONSIBLE: Kasper Telkamp Nielsen, s170397.

def dataToGrades(data):
    
    #Counting number of columns
    numcol = len(data[0,:])
    
    #Adding all of the grades to one dataframe
    grades = (data[:,2:numcol].astype(int)) 
    
    return grades