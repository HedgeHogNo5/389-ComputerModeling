import numpy as np
from Classes import Pendulum, Particle

# Create a Pendulum object with length 1 meter and mass 1 kilogram
pendulum = Pendulum(length=1, mass=1)

# Set the time step and total time for the simulation
deltaT = 0.01
total_time = 100

# Create empty arrays to store the time and position data
time_data = np.arange(0, total_time, deltaT)
position_data = np.zeros((len(time_data), 3))

# Simulate the pendulum and save the position data
for i in range(len(time_data)):
    pendulum.update(deltaT)
    position_data[i] = pendulum.particles_list[0].position

# Save the time and position data to a txt file
np.savetxt('pendulum_position.txt', np.column_stack((time_data, position_data)))
