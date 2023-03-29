import numpy as np
import matplotlib.pyplot as plt
from Classes import NewtonsCradle, Particle

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

num_particles = newtonscradle.NUM_BALLS

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
    newtonscradle.collision_detection()
    newtonscradle.FOTIerror()
    for j, particle in enumerate(newtonscradle.particles_list):
        particle.Euler(dt)
        pos[j, i] = particle.position
        pos_mag[j, i] = np.linalg.norm(particle.position)
        vel[j, i] = particle.velocity
        vel_mag[j, i] = np.linalg.norm(particle.velocity)
        accel[j, i] = particle.acceleration
        accel_mag[j, i] = np.linalg.norm(particle.acceleration)

# Plot the position, velocity, and acceleration of Particle_1 and Particle_2
fig, axs = plt.subplots(2, 3, sharex=True, figsize=(12, 8))
fig.suptitle('Position, Velocity, and Acceleration of Newton\'s Cradle Particles vs Time')

axs[0, 0].plot(t, pos[0, :, 0], label='Particle 1')
axs[0, 0].plot(t, pos[1, :, 0], label='Particle 2')
axs[0, 0].legend()
axs[0, 0].set_ylabel('Position (m)')

axs[0, 1].plot(t, vel[0, :, 0], label='Particle 1')
axs[0, 1].plot(t, vel[1, :, 0], label='Particle 2')
axs[0, 1].legend()
axs[0, 1].set_ylabel('Velocity (m/s)')

axs[0, 2].plot(t, accel[0, :, 0], label='Particle 1')
axs[0, 2].plot(t, accel[1, :, 0], label='Particle 2')
axs[0, 2].legend()
axs[0, 2].set_ylabel('Acceleration (m/s^2)')

# Hide the third row of subplots
axs[1, 0].axis('off')
axs[1, 1].axis('off')
axs[1, 2].axis('off')

plt.tight_layout()

plt.show()