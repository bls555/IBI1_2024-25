# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation #to make dynamic animation


# make array of all susceptible population
population = np.zeros( (100, 100) )
beta = 0.3 #infection rate
gamma = 0.05 #recovery rate

outbreak = np.random. choice(range(100) ,2)
population [ outbreak [0] , outbreak [1]] = 1

plt.title("2D Spatial SIR Model")
plt.xlabel("X Position")
plt.ylabel("Y Position")
#plt.figure(figsize =(6,4),dpi=150)
#img=plt.imshow(population, cmap= 'viridis', interpolation='nearest' )
#img.set_clim(vmin=0, vmax=2)
#plt.colorbar(ticks=[0,1,2], label='0=susceptible, 1=infected, 2=recovered')
#plt.title('Day 0')
cmap = cm.colors.ListedColormap(['purple', 'cyan', 'yellow'])
bounds = [0, 1, 2, 3]
norm = cm.colors.BoundaryNorm(bounds, cmap.N)

for t in range(100):

    for i in range(100):
        for j in range(100):
            if population[i,j] == 1: #if the cell is infected
                for k in range(-1,2):
                    for l in range(-1,2):
                        if i+k>=0 and i+k<100 and j+l>=0 and j+l<100:
                            if population[i+k,j+l]==0: #if the cell is susceptible
                                if np.random.choice([0,1], p=[1-beta, beta])==1:
                                    population[i+k,j+l]=1
                if np.random.choice([0,1], p=[1-gamma, gamma])==1:
                    population[i,j]=2 #if the cell is recovered

    # Plot current state
    plt.clf()
    plt.imshow(population, cmap=cmap, norm=norm, interpolation='nearest')
    plt.title(f"2D Spatial SIR Model - Time Step {t}")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.colorbar(ticks=[0.5, 1.5, 2.5], label='State', 
            boundaries=bounds, values=[0, 1, 2])
    plt.pause(0.1) # Pause to see the plot

    
plt.show()
#


