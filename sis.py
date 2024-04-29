import numpy as np
import matplotlib.pyplot as plt
import euler

# Define parameters
N = 100  # Population size
b = 0.2   # Infection rate
g = 0.1   # Recovery rate

# Define the SIR model function
def fSIS(t, x):
    x1, x2 = x[0], x[1]
    return np.array([-b*x1*x2 + g*x2, b*x1*x2 - g*x2])

# Define initial conditions
x0 = np.array([N-1, 1])  # Initial susceptible (999) and infectious (1) individuals

# Define time points
T = 10  # Total duration of simulation
dt = 0.1  # Time step
time_vect = np.linspace(0, T, int(T/dt) + 1)

# Solve using the wanted method
#solution_explicit = euler.explicit(fSIS, x0, time_vect)
#solution_implicit = euler.implicit(fSIS, x0, time_vect)
solution_mid_point = euler.mid_point(fSIS, x0, time_vect)

# Plotting
plt.figure(figsize=(N, N))
#plt.plot(solution_explicit[0], solution_explicit[1], label='Explicit', color='blue')
#plt.plot(solution_implicit[0], solution_implicit[1], label='Implicit', color='red')
#plt.plot(solution_mid_point[0], solution_mid_point[1], label='Midpoint', color='green')

plt.plot(time_vect, solution_mid_point[0], label='Susceptible_Mid_Point', color='green')
plt.plot(time_vect, solution_mid_point[1], label='Infectious_Mid_Point', color='red')

#plt.xlabel('Susceptible')
#plt.ylabel('Infectious')
#plt.title('SIR Model Phase Portrait')

plt.xlabel('Time')
plt.ylabel('Population')
plt.title('SIS Model Simulation')

plt.legend()
plt.show()
