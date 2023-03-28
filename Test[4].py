import numpy as np
import matplotlib.pyplot as plt
from Classes import NewtonsCradle, Particle

# Define the parameters of the Newton's Cradle
num_particles = 5
length = 10
mass = 1
radius = 2.5

# Create the pendulum object with the specified number of particles
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


# Simulate the movement of the Newton's Cradle
dt = 0.00001
x = 2*(newtonscradle.Period())
t = np.arange(0, x, dt)

num_steps = len(t)
pos = np.zeros((num_particles, num_steps, 3))
pos_mag = np.zeros((num_particles, num_steps))
vel = np.zeros((num_particles, num_steps, 3))
vel_mag = np.zeros((num_particles, num_steps))
accel = np.zeros((num_particles, num_steps, 3))
accel_mag = np.zeros((num_particles, num_steps))

for i in range(num_steps):
    newtonscradle.movement()
    newtonscradle.FOTIerror()
    for j, particle in enumerate(newtonscradle.particles_list):
        particle.Euler(dt)
        pos[j, i] = particle.position
        pos_mag[j, i] = np.linalg.norm(particle.position)
        vel[j, i] = particle.velocity
        vel_mag[j, i] = np.linalg.norm(particle.velocity)
        accel[j, i] = particle.acceleration
        accel_mag[j, i] = np.linalg.norm(particle.acceleration)

# Plot the position, velocity, and acceleration of each particle
fig, axs = plt.subplots(num_particles, 3, sharex=True, figsize=(12, 8*num_particles))
fig.suptitle('Position, Velocity, and Acceleration of Newton\'s Cradle Particles vs Time')

for j in range(num_particles):
    axs[j, 0].plot(t, pos[j, :, 0], label='x')
    axs[j, 0].legend()
    axs[j, 0].set_ylabel('Position (m)')

    axs[j, 1].plot(t, vel[j, :, 0], label='x')
    axs[j, 1].legend()
    axs[j, 1].set_ylabel('Velocity (m/s)')

    axs[j, 2].plot(t, accel[j, :, 0], label='x')
    axs[j, 2].legend()
    axs[j, 2].set_ylabel('Acceleration (m/s^2)')

plt.tight_layout()

# Plot the magnitude of position, velocity, and acceleration of each particle
fig, axs = plt.subplots(num_particles, 3, sharex=True, figsize=(12, 8*num_particles))
fig.suptitle('Magnitude of Position, Velocity, and Acceleration of Newton\'s Cradle Particles vs Time')

for j in range(num_particles):
    axs[j, 0].plot(t, pos_mag[j, :], label='Position')
    axs[j, 0].legend()
    axs[j, 0].set_ylabel('Position Magnitude (m)')

    axs[j, 1].plot(t, vel_mag[j, :], label='Velocity')
    axs[j, 1].legend()
    axs[j, 1].set_ylabel('Velocity Magnitude (m/s)')

    axs[j, 2].plot(t, accel_mag[j, :], label='Acceleration')
    axs[j, 2].legend()
    axs[j, 2].set_ylabel('Acceleration Magnitude (m/s^2)')

plt.tight_layout()
plt.show()