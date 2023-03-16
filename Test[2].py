import numpy as np
from Classes import NewtonsCradle,Particle

Sol = Particle(
    position=np.array([0, 0, 0], dtype = float), #As taken on the 6th of December 2021
    velocity=np.array([0, 0, 0], dtype = float), #As taken on the 6th of December 2021
    acceleration=np.array([0, 0, 0], dtype = float),
    name="Sol",
    mass= 1,
    radius= 2.5
)

NewtonsCradle.particles_list =[]

for particle in NewtonsCradle.particles_list:
    print(particle.position)
    print(particle.velocity)
    print(particle.acceleration)


NewtonsCradle.movement()
for particle in NewtonsCradle.particles_list:
    for i in range (1, 10000):
        particle.EulerCromer(0.1)
        for particle in NewtonsCradle.particles_list:
            print("position = {}".format(particle.position))
            print("Velocity = {}".format(particle.velocity))
            print("Acceleration = {}".format(particle.acceleration))