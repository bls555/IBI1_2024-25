# import libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000 #total population
beta = 0.3 #infection rate
gamma = 0.05 #recovery rate
susceptible = 9999 #initial number of susceptible individuals
infected = 1
recovered = 0

#initialize the arrays
N_list = []
susceptible_list = []
infected_list = []
recovered_list = []
time = []

#initialize the time
t = 0

#initialize the rates

susceptible_list.append(9999)
infected_list.append(1)
recovered_list.append(0)
time.append(0)
N_list.append(10000)

while t<1000:
    sup=susceptible
    inf=infected
    rec=recovered
    for i in range(0,sup):
        if np.random.choice([0,1], p=[1-beta*inf/N, beta*inf/N])==1:
            infected+=1
            susceptible-=1
    for i in range(0,inf):
        if np.random.choice([0,1], p=[1-gamma, gamma])==1:
            recovered+=1
            infected-=1
    t+=1
    time.append(t)
    N_list.append(susceptible+infected+recovered)
    susceptible_list.append(susceptible)
    infected_list.append(infected)
    recovered_list.append(recovered)


#print(N_list)

plt.plot(time, susceptible_list, label='Susceptible')
plt.plot(time, infected_list, label='Infected')
plt.plot(time, recovered_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of individuals')
plt.legend()
plt.title('SIR model')
plt.show()



