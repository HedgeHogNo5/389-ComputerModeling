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
dt = 0.001
x = 2 * (newtonscradle.Period())
t = np.arange(0, x, dt)
num_steps = len(t)
kinetic_energy = np.zeros(num_steps)
momentum = np.zeros(num_steps)

for i in range(num_steps):
    newtonscradle.movement()
    newtonscradle.collision_detection()
    newtonscradle.FOTIerror()
    for j in range(newtonscradle.NUM_BALLS):
        newtonscradle.particles_list[j].Euler(dt)
    kinetic_energy[i] = newtonscradle.TotKineticEnergy()
    momentum[i] = newtonscradle.TotMomentum()

# Plot kinetic energy and momentum
fig, axs = plt.subplots(2, sharex=True, figsize=(10, 6))
axs[0].plot(t[1:], kinetic_energy[1:], label="Kinetic Energy")
axs[0].set_ylabel("Energy (J)")
axs[0].legend()
axs[1].plot(t, momentum, label="Momentum")
axs[1].set_ylabel("Momentum (kg m/s)")
axs[1].set_xlabel("Time (s)")
axs[1].legend()

plt.show()
