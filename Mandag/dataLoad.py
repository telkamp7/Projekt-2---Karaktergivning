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
    
    return(data)