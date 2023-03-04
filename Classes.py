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
        return "Particle: {0}, Mass: {1}, Position: {2}, Velocity: {3}, Acceleration: {4}, gravitational Acceleration{5}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration, self.g
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

    def collision_detection(self, DeltaT):
        for particle in self.particles_list:

    def movement(self, deltaT):

        for i in range(self.NUM_BALLS):
            equilibrium = np.array([i * self.SPACING, self.CHAIN_LENGTH, 0])

            for particle in self.particles_list:
                angle = np.arccos(np.dot(particle.position, equilibrium)/(np.linalg.norm(particle.position) * np.linalg.norm(equilibrium)))
                particle.acceleration = np.array([np.linalg.norm(particle.g) * np.sin(angle), np.linalg.norm(particle.g) * np.cos(angle), 0])
                # update particle position and velocity
                particle.EulerCromer(deltaT)


class Pendulum(NewtonsCradle):

    def __init__(self, length, mass):
        self.length = length
        self.mass = mass
        self.BALL_RADIUS = 2.5
        self.NUM_BALLS = 1
        self.particles_list = [Particle(
            position=np.array([0.0, -self.length, 0.0], dtype=float),
            velocity=np.array([0.0, 0.0, 0.0], dtype=float),
            acceleration=np.array([0.0, 0.0, 0.0], dtype=float),
            name='Ball',
            mass=self.mass,
            g=np.array([0, -9.81, 0])
        )]
        self.SPACING = 2 * self.BALL_RADIUS
        self.g = np.array([0, -9.81, 0])  # in metres per second^2 using a approximation

        super().__init__(self.particles_list)
    def update(self, deltaT):
        self.collision_detect(deltaT)
        particle = self.particles_list[0]
        theta = np.arcsin(-particle.position[1] / self.length)
        alpha = -self.g[1] / self.length * np.sin(theta)
        particle.acceleration[0] = -alpha * np.sin(theta)