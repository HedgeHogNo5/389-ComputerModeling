import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt("/Users/samuelhedges/Documents/GitHub/389-ComputerModeling/pendulum_position.txt")

# Plot position vs. time
plt.plot(data[:, 0], data[:, 1])
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.title("Pendulum Motion")
plt.show()
