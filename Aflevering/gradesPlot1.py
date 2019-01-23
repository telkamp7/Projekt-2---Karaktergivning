"""
GRADESPLOT
The purpose of this function is to generate two plots: one bar plot of the 
distribution of grades one diagram with the assignments of the x-axis, the 
grades on the y-axis and dots representing the given grades.

INPUT: grades: matrix containing all given grades.

SCREEN OUTPUT: one bar plot and one diagram with dots in separate figure 
               windows.
    
The whole assignment has been worked out by the whole group in collaboration,
but it has been divided into sections, each with a responsible group member.

RESPONSIBLE: Freja Terp Petersen, s184321.

"""
#   Importing packages and the computeFinalGrades function.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from computeFinalGrades import computeFinalGrades

def gradesPlot(grades):
    
    ### Bar plot
    
    
    #   Defining the final grades as a vector using the computeFinalGrades 
    #   function.
    finalGrades = computeFinalGrades(grades)

    #   Defining empty vector which is filled with counts.
    counts = np.array([])
    #   Defining the grading scale as a vector.
    gradeScale = np.array([-3,0,2,4,7,10,12])
    #For-loop which counts frequencies of grades.
    for i in gradeScale:
        #   When an element in the 'finalGrades' vector equals an element in 
        #   the grading scale (i), the frequency of the element in 'finalGrades' 
        #   will be put into the 'counts' vector by np.count_nonzero.
        counts = np.append(counts, np.count_nonzero(finalGrades == i)).astype(int)
    
    #   Vectors, which names the ticks and decides their position.
    tickshist = ("-3","00","02","4","7","10","12")
    ticksposhist = np.arange(1, 8)
    
    #   Bar plot settings.
    plt.bar(ticksposhist, counts, edgecolor = "black", color = "skyblue", width = 0.7)
    #   We want to use the above defined ticks.
    plt.xticks(ticksposhist, tickshist)
    #   The ticks on the y-axis must only contain integers.
    plt.yticks(np.arange(0, max(counts) + 1))
    #   Title and axis labels.
    plt.title("Final Grades")
    plt.ylabel("Number of Students")
    plt.xlabel("Grades")
    #   Show plot.
    plt.show()
    
    #-------------------------------------------------------------------------
    
    ###Scatter plot
    
    #   Defining scalar with number of assignments.
    num_assignments = len(grades[0,:])
    
    #   Variables which control the making of legend labels.
    v = 0
    inv = 0
    mea = 0
    
    #   For-loop which determines the mean grades for each assignment.
    for i in range(num_assignments):
        
        #   Calculate means
        avrg = np.mean(grades[:,i])
        #   We make a line for each mean value. 
        xvec = np.array([i+1-0.25, i+1, i+1+0.25])
        yvec = np.array([avrg,avrg,avrg])
        
        #   Plotting mean lines.
        #   If the mea-variable is zero, the mean line will be assigned a label.
        if mea == 0:
            plt.plot(xvec, yvec, "g--", label = "Mean Grade")
            mea += 1
        #   If the mea-variable has a value above zero, the mean line will be 
        #   plotted without label
        else:
            plt.plot(xvec, yvec, "g--")
        
        #   For-loop which plots the grades (both valid and, if present, invalid)
        for j in grades[:,i]:
            #   We plot with blue stars, if j is element in 'gradeScale'. 
            if np.any(j == gradeScale):
                #   In the same way, the labels of these plots depend on the 
                #   variables v and inv. 
                if v == 0:
                    #   v = 0: label will be assigned to plot.
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i + 1 + var, j + var, "b*", label = "Grades")
                    v += 1
                else:
                    #   v != 0: label will not be assigned to plot.
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i + 1 + var, j + var, "b*")
                    
            #   We plot with red stars, if j is not element in 'gradeScale'. 
            else:
                if inv == 0:
                    #   inv = 0: label will be assigned to plot.
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i+1 + var, j + var, "r*", label = "Invalid Grades")
                    inv += 1
                else:
                    #   inv != 0: label will not be assigned to plot.
                    var = np.asscalar(np.random.uniform(-0.1, 0.1, 1))
                    plt.plot(i+1 + var, j + var, "r*")
        

        
    #   Plot settings.
    #   Plot title and labels for axes.
    plt.title("Grades per assignment")
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    #   We use our own ticks.
    #   The grading scale on the y-axis.
    plt.yticks(gradeScale, tickshist)
    #   The assignment numbers on the x-axis.
    plt.xticks(np.arange(1, num_assignments+1, 1))
    plt.xlim(0,num_assignments + 1)
    #   We place the legends to the right of the plot window.
    plt.legend(bbox_to_anchor = (1.05, 1), loc = 2,  borderaxespad = 0) 
    #   Show plot. 
    plt.show()
    
    print("Above you can see 2 diagrams. The first plot is a bar plot that shows the final grades and the number of students who got it.\nThe second diagram is a plot that shows the grade as well as the meangrade for each assignment.\n")

    if inv != 0:        
        print("Note that there are one or more invalid grades in the data set")
        print("This may affect the mean lines as well as the final grades plot.\n")



