import numpy as np
import matplotlib.pyplot as plt
from Classes import Pendulum, Particle

pendulum = Pendulum(length=10, mass=1, radius=2.5, psi=np.pi/12)

# Simulate the pendulum movement
dt = 0.0001
x=100
t = np.arange(0, x, dt)

num_steps = len(t)
pos = np.zeros((num_steps, 3))
pos_mag = np.zeros(num_steps)
vel = np.zeros((num_steps, 3))
accel = np.zeros((num_steps, 3))
accel_mag = np.zeros(num_steps)

for i in range(num_steps):
    for particle in pendulum.particles_list:
        pendulum.movement()
        """pendulum.FOTIerror()"""
        particle.Euler(dt)
        pos[i] = particle.position
        pos_mag[i] = np.linalg.norm(particle.position)
        vel[i] = particle.velocity
        accel[i] = particle.acceleration
        accel_mag[i] = np.linalg.norm(particle.acceleration)

# Plot x, y, z components, and magnitude of position
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=True, figsize=(12, 8))
fig.suptitle('Position and Acceleration of First Particle in Pendulum vs Time')

ax1.plot(t, pos[:, 0], label='x')
ax1.legend()
ax1.set_ylabel('Position (m)')

ax2.plot(t, pos[:, 1], label='y')
ax2.legend()
ax2.set_ylabel('Position (m)')

ax3.plot(t, pos[:, 2], label='z')
ax3.legend()
ax3.set_ylabel('Position (m)')

ax4.plot(t, accel[:, 0], label='x')
ax4.legend()
ax4.set_ylabel('Acceleration (m/s^2)')

ax5.plot(t, accel[:, 1], label='y')
ax5.legend()
ax5.set_ylabel('Acceleration (m/s^2)')

ax6.plot(t, accel[:, 2], label='z')
ax6.legend()
ax6.set_ylabel('Acceleration (m/s^2)')

plt.tight_layout()

# Plot magnitude of position and acceleration
fig, (ax7, ax8) = plt.subplots(2, 1, sharex=True, figsize=(8, 8))

ax7.plot(t, pos_mag, label='magnitude')
ax7.legend()
ax7.set_xlabel('Time (s)')
ax7.set_ylabel('Position (m)')

ax8.plot(t, accel_mag, label='magnitude')
ax8.legend()
ax8.set_xlabel('Time (s)')
ax8.set_ylabel('Acceleration (m/s^2)')

plt.tight_layout()
plt.show()
