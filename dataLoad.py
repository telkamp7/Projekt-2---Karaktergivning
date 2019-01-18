import pandas as pd
import numpy as np




def dataLoad(filename):
    """
    Reads csv file to dataframe.
    Sorts the dataframe alphabetically by names.
    Separates numbers and strings.
    Numbers are put in matrix. 
    Output is ???
    
    """
    
    
    #Reading data
    data = pd.read_csv(filename)
    
    #Using argsort to get index from sorted values. 
    index = data.Name.values.astype(str).argsort()
    #Sorting, using the indices
    #https://stackoverflow.com/questions/43401903/python-order-dataframe-alphabetically
    data = pd.DataFrame(data.values[index], data.index[index], data.columns)
    
    #Counting number of columns
    numcol = len(data.columns)
    
    #Adding all of the grades to one dataframe
    datagrade = (data.iloc[:,2:numcol].astype(int))
    #Converting into matrix
    grades = np.array(datagrade)
    

    return(data)