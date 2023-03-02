import numpy as np

class Particle:
    """In this script we are creating a single class called Particle.
    This Particle will be the basis for the masses of the Newton's Cradel


    This class needs to have clear variables:
    Position (representing the position as a vector);
    Velocity (representing the velocity as a vector);
    and acceleration (representing the acceleration as a vector)
    as well as mass which is a scalar quantity
    """

    def __init__(
            self,
            position=np.array([0.0, 0.0, 0.0], dtype=float),
            velocity=np.array([0.0, 0.0, 0.0], dtype=float),
            acceleration=np.array([0.0, 0.0, 0.0], dtype=float),
            name='Ball',  # name of the object
            mass=1.0,  # Currently in Kilograms (Kg)
            g = np.array([0, -9.81, 0]) #in metres per second^2 using a approximation
    ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.g = g
        #Defining the names and other variables of the Particle

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def Euler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT
        #This updates the position of any body passed through this class using using the Euler Numerical method

    def EulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
        # This updates the position of any body passed through this class using using the Euler-Cromer Numerical method



class NewtonsCradle:
    def __init__(self, particles_list):
        self.particles_list = particles_list
        self.BALL_RADIUS = 2.5
        self.NUM_BALLS = len(particles_list)
        self.CHAIN_LENGTH = 10
        self.SPACING = 2 * self.BALL_RADIUS
        self.g = np.array([0, -9.81, 0])  # in metres per second^2 using a approximation

            # calculate gravity
            gravity = np.array([0.0, -particle.mass * self.g, 0.0], dtype=float)

            # calculate acceleration
            acceleration = tension + gravity
            particle.acceleration = acceleration

        # update position and velocity of each particle
        self.collision_detect(deltaT)

    def collision_detect(self, deltaT):
        for i in range(self.NUM_BALLS-1):
            # check if balls are touching
            dist = np.linalg.norm(self.particles_list[i + 1].position - self.particles_list[i].position)
            if dist < self.SPACING:
                # calculate new velocities
                v1 = self.particles_list[i].velocity
                v2 = self.particles_list[i + 1].velocity
                m1 = self.particles_list[i].mass
                m2 = self.particles_list[i + 1].mass
                u1 = ((m1 - m2) / (m1 + m2)) * v1 + ((2 * m2) / (m1 + m2)) * v2
                u2 = ((m2 - m1) / (m1 + m2)) * v2 + ((2 * m1) / (m1 + m2)) * v1
                self.particles_list[i].velocity = u1
                self.particles_list[i + 1].velocity = u2

        for particle in self.particles_list:
            # update particle position and velocity
            particle.EulerCromer(deltaT)






