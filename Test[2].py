import numpy as np
import matplotlib.pyplot as plt
from Classes import NewtonsCradle, Particle

Particle_1 = Particle(
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Particle 1",
    mass=1,
    radius=2.5
)
Particle_2 = Particle(
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Particle 2",
    mass=1,
    radius=2.5
)
pl = [Particle_1, Particle_2]
newtonscradle = NewtonsCradle(particles_list=pl, length=10, psi=np.pi/12)

# Simulate the pendulum movement
# Simulate the pendulum movement
dt = 0.001
x = 2 * (newtonscradle.Period())
t = np.arange(0, x, dt)
num_steps = len(t)
pos = np.zeros((num_steps, newtonscradle.NUM_BALLS, 3))
pos_mag = np.zeros(num_steps)
vel = np.zeros((num_steps, newtonscradle.NUM_BALLS, 3))
vel_mag = np.zeros(num_steps)
acc = np.zeros((num_steps, newtonscradle.NUM_BALLS, 3))
acc_mag = np.zeros(num_steps)

for i in range(num_steps):
    newtonscradle.movement()
    newtonscradle.collision_detection()
    newtonscradle.FOTIerror()
    for j in range(newtonscradle.NUM_BALLS):
        newtonscradle.particles_list[j].Euler(dt)
        pos[i, j] = newtonscradle.particles_list[j].position
        vel[i, j] = newtonscradle.particles_list[j].velocity
        acc[i, j] = newtonscradle.particles_list[j].acceleration
        pos_mag[i] += np.linalg.norm(pos[i, j, :])**2
        vel_mag[i] += np.linalg.norm(vel[i, j, :])**2
        acc_mag[i] += np.linalg.norm(acc[i, j, :])**2

    pos_mag[i] = np.sqrt(pos_mag[i])
    vel_mag[i] = np.sqrt(vel_mag[i])
    acc_mag[i] = np.sqrt(acc_mag[i])

# Plot position, velocity, and acceleration
fig, axs = plt.subplots(4, sharex=True, figsize=(10, 10))
axs[0].plot(t, pos[:, 0], label="Particle 1")
axs[0].plot(t, pos[:, 1], label="Particle 2")
axs[0].set_ylabel("Position (m)")
axs[0].legend()
axs[1].plot(t, vel[:, 0], label="Particle 1")
axs[1].plot(t, vel[:, 1], label="Particle 2")
axs[1].set_ylabel("Velocity (m/s)")
axs[1].legend()
axs[2].plot(t, acc[:, 0], label="Particle 1")
axs[2].plot(t, acc[:, 1], label="Particle 2")
axs[2].set_ylabel("Acceleration (m/s^2)")
axs[2].legend()
axs[3].plot(t, pos_mag, label="Position Magnitude")
axs[3].plot(t, vel_mag, label="Velocity Magnitude")
axs[3].plot(t, acc_mag, label="Acceleration Magnitude")
axs[3].set_xlabel("Time (s)")
axs[3].set_ylabel("Magnitude")
axs[3].legend()

plt.show()
