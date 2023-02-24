import numpy as np
from Classes import Particle, NewtonsCradle

# create two particles
p1 = Particle(position=[0, 10, 0], velocity=[1, 0, 0], mass=2)
p2 = Particle(position=[5, 10, 0], velocity=[0, 0, 0], mass=2)

# create a Newton's Cradle with the particles
nc = NewtonsCradle([p1, p2])

# simulate the Newton's Cradle for 10 seconds with a time step of 0.01 seconds
for i in range(1000):
    nc.update(0.01)
    print("Particle 1:", p1.position)
    print("Particle 2:", p2.position)