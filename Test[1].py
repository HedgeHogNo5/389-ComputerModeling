import numpy as np
import matplotlib.pyplot as plt
from Classes import Pendulum, Particle

pendulum = Pendulum(length=10, mass=1, radius=2.5, psi=np.pi/8)

# Simulate the pendulum movement
dt = 0.1
x=100000
t = np.arange(0, x, dt)
num_steps = len(t)
pos = np.zeros((num_steps, 3))

for particle in pendulum.particles_list:
    for i in range(num_steps):
        pendulum.movement()
        particle.EulerCromer(dt)
        pos[i] = particle.position
        print("position = {}".format(particle.position))
        print("Velocity = {}".format(particle.velocity))
        print("Acceleration = {}".format(particle.acceleration))

# Plot x, y, and z components of position separately
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(8, 8))
fig.suptitle('Position of First Particle in Pendulum vs Time')

ax1.plot(t, pos[:, 0], label='x')
ax1.legend()
ax1.set_ylabel('Position (m)')

ax2.plot(t, pos[:, 1], label='y')
ax2.legend()
ax2.set_ylabel('Position (m)')

ax3.plot(t, pos[:, 2], label='z')
ax3.legend()
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Position (m)')

plt.show()