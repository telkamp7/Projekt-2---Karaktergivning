import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from computeFinalGrades import computeFinalGrades

#RESPONSIBLE: Freja Terp Petersen, s184321.

def gradesPlot(grades):
    finalGrades = computeFinalGrades(grades)

    #For-loop which counts frequencies of grades.
    counts = np.array([])
    gradeScale = np.array([-3,0,2,4,7,10,12])
    for i in gradeScale:
        counts = np.append(counts, np.count_nonzero(finalGrades == i)).astype(int)
    
    #Vectors, which names the ticks and decides their position.
    tickshist = ("-3","00","02","4","7","10","12")
    ticksposhist = np.arange(1, 8)
    
    #Plotting the histogram
    plt.bar(ticksposhist, counts, edgecolor = "black", color = "skyblue", width = 0.7)
    plt.xticks(ticksposhist, tickshist)
    plt.yticks(np.arange(0, max(counts) + 1))
    plt.title("Final Grades")
    plt.ylabel("Number of Students")
    plt.xlabel("Grades")
    plt.show()
    
    
    #Defining scalar with number of assignments.
    num_assignments = len(grades[0,:])
    
    #Variables which control the making of legend labels.
    v = 0
    inv = 0
    mea = 0
    
    #Making for-loop which determines the mean grades for each assignment.
    for i in range(num_assignments):
        
        #Calculate means
        avrg = np.mean(grades[:,i])
        #We make a line for each mean value. 
        xvec = np.array([i+1-0.25, i+1, i+1+0.25])
        yvec = np.array([avrg,avrg,avrg])
        
        #Plotting mean lines.
        #If the mea-variable is zero, the mean line will be assigned a label.
        if mea == 0:
            plt.plot(xvec, yvec, "g--", label = "Mean Grade")
            mea += 1
        #If the mea-variable has a value above zero, the mean line will be plotted without label
        else:
            plt.plot(xvec, yvec, "g--")
        
        #For-loop which plots the grades (both valid and invalid)
        for j in grades[:,i]:
            #We plot with blue stars, if j is element in the gradeScale. 
            if np.any(j == gradeScale):
                #In the same way, the labels of these plots depend on the variables v and inv. 
                if v == 0:
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i + 1 + var, j + var, "b*", label = "Grades")
                    v += 1
                else:
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i + 1 + var, j + var, "b*")
            #We plot with red stars, if j is element in the gradeScale. 
            else:
                if inv == 0:
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i+1 + var, j + var, "r*", label = "Invalid Grades")
                    inv += 1
                else:
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i+1 + var, j + var, "r*")
    
    #Plot settings.
    plt.title("Grades per assignment")
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.yticks(gradeScale, tickshist)
    plt.xticks(np.arange(1, num_assignments+1, 1))
    plt.xlim(0,num_assignments + 1)
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 2,  borderaxespad = 0) 
    plt.show()





