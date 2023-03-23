import numpy as np
import matplotlib.pyplot as plt
from Classes import Pendulum, Particle

pendulum = Pendulum(length=10, mass=1, radius=2.5, psi=np.pi/12)

# Simulate the pendulum movement
dt = 0.00001
x = 1*(pendulum.Period())
t = np.arange(0, x, dt)

num_steps = len(t)
pos = np.zeros((num_steps, 3))
pos_mag = np.zeros(num_steps)
vel = np.zeros((num_steps, 3))
vel_mag = np.zeros(num_steps)
accel = np.zeros((num_steps, 3))
accel_mag = np.zeros(num_steps)

for i in range(num_steps):
    for particle in pendulum.particles_list:
        pendulum.movement()
        pendulum.FOTIerror()
        particle.Euler(dt)
        pos[i] = particle.position
        pos_mag[i] = np.linalg.norm(particle.position)
        vel[i] = particle.velocity
        vel_mag[i] = np.linalg.norm(particle.velocity)
        accel[i] = particle.acceleration
        accel_mag[i] = np.linalg.norm(particle.acceleration)

# Plot x, y, z components, and magnitude of position, velocity, and acceleration
fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, sharex=True, figsize=(12, 8))
fig.suptitle('Position, Velocity, and Acceleration of First Particle in Pendulum vs Time')

ax1.plot(t, pos[:, 0], label='x')
ax1.legend()
ax1.set_ylabel('Position (m)')

ax2.plot(t, pos[:, 1], label='y')
ax2.legend()
ax2.set_ylabel('Position (m)')

ax3.plot(t, pos[:, 2], label='z')
ax3.legend()
ax3.set_ylabel('Position (m)')

ax4.plot(t, vel[:, 0], label='x')
ax4.legend()
ax4.set_ylabel('Velocity (m/s)')

ax5.plot(t, vel[:, 1], label='y')
ax5.legend()
ax5.set_ylabel('Velocity (m/s)')

ax6.plot(t, vel[:, 2], label='z')
ax6.legend()
ax6.set_ylabel('Velocity (m/s)')

ax7.plot(t, accel[:, 0], label='x')
ax7.legend()
ax7.set_ylabel('Acceleration (m/s^2)')

ax8.plot(t, accel[:, 1], label='y')
ax8.legend()
ax8.set_ylabel('Acceleration (m/s^2)')

ax9.plot(t, accel[:, 2], label='z')
ax9.legend()
ax9.set_ylabel('Acceleration (m/s^2)')

plt.tight_layout()

# Plot magnitude of position, velocity, and acceleration
fig, (ax10, ax11, ax12) = plt.subplots(3, 1, sharex=True, figsize=(8, 12))

ax10.plot(t, pos_mag, label='Position')
ax10.legend()
ax10.set_ylabel('Position Magnitude (m)')

ax11.plot(t, vel_mag, label='Velocity')
ax11.legend()
ax11.set_ylabel('Velocity Magnitude (m/s)')

ax12.plot(t, accel_mag, label='Acceleration')
ax12.legend()
ax12.set_xlabel('Time (s)')
ax12.set_ylabel('Acceleration Magnitude (m/s^2)')

plt.tight_layout()
plt.show()

