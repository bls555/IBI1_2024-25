import numpy as np
import matplotlib.pyplot as plt

# parameters
beta = 0.3   # 
gamma = 0.05  # 
N = 10000    # 
I0 = 1     # infected
R0 = 0       # recovered
S0 = N - I0 - R0  # susceptible

# rime arrangement
total_time = 1000  # 
dt = 1          # 
time = np.arange(0, total_time, dt)

# vaccination
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# color arrangement
colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

# 
infected_data = []

# core
for rate, color in zip(vaccination_rates, colors):
    # 
    S = S0 * (1 - rate)
    I = I0
    R = R0 + S0 * rate
    infected = [I]
    
    for t in time[1:]:
        # 
        dS = -beta * S * I / N #derta S
        dI = beta * S * I / N - gamma * I #derta I
        dR = gamma * I
        
        S += dS * dt
        I += dI * dt
        R += dR * dt
        
        infected.append(I)
    
    infected_data.append(infected)

# plot
plt.figure(figsize=(10, 7))
for i, rate in enumerate(vaccination_rates):
    plt.plot(time, infected_data[i], label=f'{int(rate*100)}%', color=colors[i])

plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR model with different vaccination rates')
plt.legend(title='Vaccination Rate', bbox_to_anchor=(0.8, 1), loc='upper left')
plt.grid(True)
plt.show()