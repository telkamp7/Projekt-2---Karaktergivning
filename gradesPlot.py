import numpy as np
import matplotlib.pyplot as plt
from computeFinalGrades import computeFinalGrades

def gradesPlot(grades):
    finalGrades = computeFinalGrades(grades)

    #For-loop which counts frequencies of grades.
    counts = np.array([])
    gradeScale = np.array([-3,0,2,4,7,10,12])
    for i in gradeScale:
        counts = np.append(counts, list(finalGrades).count(i)).astype(int)
    
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
    
    #Plotting the plot
    num_assignments = np.arange(0,len(data[0,:]) - 2)
    
    
    plt.plot()
    plt.title("Grades per assignment")
    plt.xlabel("Assignments")
    plt.ylabel("Grades")
    plt.xticks(num_assignments)





