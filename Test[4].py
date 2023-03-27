import numpy as np
import matplotlib.pyplot as plt
from Classes import Pendulum, Particle, NewtonCradle

cradle = NewtonCradle(num_particles=5, length=10, mass=1, radius=2.5, psi=np.pi/12)

# Simulate the Newton's Cradle movement
dt = 0.00001
x = 2*(cradle.Period())
t = np.arange(0, x, dt)

num_steps = len(t)
pos = np.zeros((num_steps, 3*cradle.num_particles))
pos_mag = np.zeros(num_steps*cradle.num_particles)
vel = np.zeros((num_steps, 3*cradle.num_particles))
vel_mag = np.zeros(num_steps*cradle.num_particles)
accel = np.zeros((num_steps, 3*cradle.num_particles))
accel_mag = np.zeros(num_steps*cradle.num_particles)

for i in range(num_steps):
    cradle.movement()
    cradle.FOTIerror()
    for j, particle in enumerate(cradle.particles_list):
        particle.Euler(dt)
        pos[i, 3*j:3*j+3] = particle.position
        pos_mag[i*cradle.num_particles+j] = np.linalg.norm(particle.position)
        vel[i, 3*j:3*j+3] = particle.velocity
        vel_mag[i*cradle.num_particles+j] = np.linalg.norm(particle.velocity)
        accel[i, 3*j:3*j+3] = particle.acceleration
        accel_mag[i*cradle.num_particles+j] = np.linalg.norm(particle.acceleration)

# Plot x, y, z components, and magnitude of position, velocity, and acceleration for each particle
fig, axs = plt.subplots(cradle.num_particles, 3, sharex=True, figsize=(12, 8*cradle.num_particles))
fig.suptitle('Position, Velocity, and Acceleration of Particles in Newton\'s Cradle vs Time')

for j in range(cradle.num_particles):
    axs[j, 0].plot(t, pos[:, 3*j], label='x')
    axs[j, 0].legend()
    axs[j, 0].set_ylabel(f'Particle {j+1} Position (m)')

    axs[j, 1].plot(t, pos[:, 3*j+1], label='y')
    axs[j, 1].legend()
    axs[j, 1].set_ylabel(f'Particle {j+1} Position (m)')

    axs[j, 2].plot(t, pos[:, 3*j+2], label='z')
    axs[j, 2].legend()
    axs[j, 2].set_ylabel(f'Particle {j+1} Position (m)')

plt.tight_layout()

# Plot magnitude of position, velocity, and acceleration for each particle
fig, axs = plt.subplots(cradle.num_particles, 3, sharex=True, figsize=(12, 8*cradle.num_particles))

for j in range(cradle.num_particles):
    axs[j, 0].plot(t, pos_mag[j*num_steps:(j+1)*num_steps], label='Position')
    axs[j, 0].legend()
    axs[j, 0].set_ylabel(f'Particle {j+1} Position Magnitude (m)')

    axs[j, 1].plot(t, vel_mag[j*num_steps:(j+1)*num_steps], label='Velocity')
    axs[j,
