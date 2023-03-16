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
            radius = 1.0, #Currently in cm
            g = np.array([0, -9.81, 0]) #in metres per second^2 using a approximation
    ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.radius = radius
        self.g = g
        #Defining the names and other variables of the Particle

    def __str__(self):
        return "Particle: {0}, Mass: {1}, Radius{2} Position: {3}, Velocity: {4}, Acceleration: {5}, gravitational Acceleration{6}".format(
            self.name, self.mass, self.radius,  self.position, self.velocity, self.acceleration, self.g
        )
    def KineticEnergy(self):
       KE = 1/2*self.mass*np.linalg.norm(self.velocity)
       return KE

    def Momentum(self):
       rho = 1/2*self.mass*np.linalg.norm(self.velocity)
       return rho
    def Euler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT
        #This updates the position of any body passed through this class using using the Euler Numerical method

    def EulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
        # This updates the position of any body passed through this class using using the Euler-Cromer Numerical method



class NewtonsCradle:
    def __init__(self, particles_list, psi):
        self.particles_list = particles_list
        self.NUM_BALLS = len(particles_list)
        self.CHAIN_LENGTH = 10
        self.Positioningx = np.zeros(self.NUM_BALLS)
        self.InitialAngle = psi

        for i in range(self.NUM_BALLS):
            self.Positioningx[0] = 0
            if i == 0:
                continue
            self.Positioningx[i]+= self.Positioningx[i-1] + self.particles_list[i-1].radius + self.Positioningx[i]

        for i in range (self.NUM_BALLS):
            self.particles_list[i].position = np.array([self.Positioningx[i], -self.CHAIN_LENGTH,0])

        if self.InitialAngle != 0:
            d = np.linalg.norm([self.Positioningx[0], -self.CHAIN_LENGTH,0])
            self.particles_list[0].position=np.array([d * np.sin(self.InitialAngle), d*np.cos(self.InitialAngle),0])



    def collision_detection(self):
       for i in range (self.NUM_BALLS):
           if np.linalg.norm(self.particles_list[i].position - self.particles_list[i+1].position) <= (self.particles_list[i].radius + self.particles_list[i+1].radius):
               for j in range(3):
                   m1 = self.particles_list[i].mass  # Mass of Fist ball in Kg
                   m2 = self.particles_list[i+1].mass  # Mass of Second ball in Kg
                   u1 = self.particles_list[i].velocity[j]  # Initial Velocity of first ball in m/s
                   u2 = self.particles_list[i+1].velocity[j]  # Initial Velocity of second ball in m/s
                   mu1 = m1 / 2  # Half mass used in Kinetic energy EQN
                   mu2 = m2 / 2  # Half mass used in Kinetic energy EQN
                   mr = m2 / m1  # Ratio of the two masses
                   a = (mu2 + mu1 * mr ** 2)
                   b = (-2 * mr * mu1 * u1 - 2 * u2 * (mr ** 2) * mu1 * u2 * mr ** 2)
                   c = 2 * mr * u1 * mu1 * u2 + mu1 * (mr ** 2) * (u2 ** 2) - mu2 * u2
                   self.particles_list[i+1].velocity[j] = (-b + np.sqrt((b ** 2) - 4 * a * c)) / 2 * a  # Quadratic formula
                   self.particles_list[i].velocity[j] = u1 + mr * (u2 - self.particles_list[i+1].velocity[j])

    def movement(self):
        for i in range(self.NUM_BALLS): #iterates all the balls in the particles_list
            equilibrium = np.array([self.Positioningx[i], -self.CHAIN_LENGTH, 0]) #defines an equalibrium position for all the particles
            for particle in self.particles_list:
                angle = np.arccos(np.dot(particle.position, equilibrium)/(np.linalg.norm(particle.position) * np.linalg.norm(equilibrium))) #Defines the angle that the particle makes to the equalibrium position
                particle.acceleration = np.array([np.linalg.norm(particle.g) * np.sin(angle) * np.sin(angle), np.linalg.norm(particle.g) *np.sin(angle) * np.cos(angle), 0]) #Creates gravitational acceleration due to a particle's displacemet
                # update particle position and velocity
    def FOTIerror(self):
        for i in range (self.NUM_BALLS):
            if np.linalg.norm(self.particles_list[i].position) > np.linalg.norm([self.Positioningx, -self.CHAIN_LENGTH, 0])
                raise Exception ("Particle flew off to infinity")
class Pendulum(NewtonsCradle):

    def __init__(self, mass, length, radius, psi):
        self.length = length
        self.InitialAngle = psi
        self.mass = mass
        self.radius = radius
        self.NUM_BALLS = 1
        self.particles_list = [Particle(
            position=np.array([0, -self.length, 0.0], dtype=float),
            velocity=np.array([0.0, 0.0, 0.0], dtype=float),
            acceleration=np.array([0.0, 0.0, 0.0], dtype=float),
            name='Ball',
            mass=self.mass,
            radius= self.radius,
            g=np.array([0, -9.81, 0])
        )]
        self.SPACING = np.zeros(1)
        super().__init__(self.particles_list, psi)



