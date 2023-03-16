import numpy as np
from Classes import Pendulum,Particle
pendulum = Pendulum(length=10, mass=1, radius=2.5, psi=np.pi / 4)

for particle in pendulum.particles_list:
    print("position = {}".format(particle.position))
    print("Velocity = {}".format(particle.velocity))
    print("Acceleration = {}".format(particle.acceleration))


pendulum.movement()
for particle in pendulum.particles_list:
    for i in range (1, 10000):
        particle.EulerCromer(0.1)
        for particle in pendulum.particles_list:
            print("position = {}".format(particle.position))
            print("Velocity = {}".format(particle.velocity))
            print("Acceleration = {}".format(particle.acceleration))
