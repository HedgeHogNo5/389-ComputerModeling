import numpy as np
import matplotlib.pyplot as plt
from Classes import Pendulum, Particle

pendulum = Pendulum(length=10, mass=1, radius=2.5, psi=np.pi/12)

# Simulate the pendulum movement
dt = 0.1
x=1000
t = np.arange(-1, x, dt)
num_steps = len(t)
pos = np.zeros((num_steps, 3))
pos_mag = np.zeros(num_steps)

for particle in pendulum.particles_list:
    for i in range(num_steps):
        pendulum.movement()
        particle.EulerCromer(dt)
        pos[i] = particle.position
        pos_mag[i] = np.linalg.norm(particle.position)
        print("position = {}".format(particle.position))
        print("Velocity = {}".format(particle.velocity))
        print("Acceleration = {}".format(particle.acceleration))

# Plot x, y, z components, and magnitude of position
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(8, 10))
fig.suptitle('Position of First Particle in Pendulum vs Time')

ax1.plot(t, pos[:, 0], label='x')
ax1.legend()
ax1.set_ylabel('Position (m)')

ax2.plot(t, pos[:, 1], label='y')
ax2.legend()
ax2.set_ylabel('Position (m)')

ax3.plot(t, pos[:, 2], label='z')
ax3.legend()
ax3.set_ylabel('Position (m)')

ax4.plot(t, pos_mag, label='magnitude')
ax4.legend()
ax4.set_xlabel('Time (s)')
ax4.set_ylabel('Position (m)')

plt.show()