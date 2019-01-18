
import pandas as pd
import numpy as np

from dataLoad import *

def dataCheck(data):
    
    
    Errs = - len(data.iloc[:,0])
    for i in data.iloc[:,0]:
        for j in data.iloc[:,0]:
            
            if j == i:
                print(i)
                Errs = Errs + 1



