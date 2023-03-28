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
            radius=1.0,  # Currently in cm
            colour=(255, 255, 255)  # RGB color value (default is white)
    ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.radius = radius
        self.colour = colour
        # Defining the names and other variables of the Particle

    def __str__(self):
        return "Particle: {0}, Mass: {1}, Radius: {2}, Position: {3}, Velocity: {4}, Acceleration: {5}, Colour: {6}".format(
            self.name, self.mass, self.radius, self.position, self.velocity, self.acceleration, self.colour
        )

    def KineticEnergy(self):
        KE = 1 / 2 * self.mass * np.linalg.norm(self.velocity)
        return KE

    def Momentum(self):
        rho = 1 / 2 * self.mass * np.linalg.norm(self.velocity)
        return rho

    def Euler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT
        # This updates the position of any body passed through this class using the Euler Numerical method

    def EulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT
        # This updates the position of any body passed through this class using the Euler-Cromer Numerical method


class NewtonsCradle:
    def __init__(self, particles_list, length, psi):
        self.particles_list = particles_list
        self.NUM_BALLS = len(particles_list)
        self.CHAIN_LENGTH = length
        self.Positioningx = np.zeros(self.NUM_BALLS)
        self.InitialAngle = psi
        self.g = [0, -9.81, 0]

        for i in range(self.NUM_BALLS):
            if i == 0:
                self.Positioningx[i]=0
            else:
                self.Positioningx[i] = self.Positioningx[i - 1] + self.particles_list[i - 1].radius + self.particles_list[
                i].radius

        for i in range(self.NUM_BALLS):
            self.particles_list[i].position = np.array([self.Positioningx[i], -self.CHAIN_LENGTH, 0])

        if self.InitialAngle != 0:
            d = self.CHAIN_LENGTH
            self.particles_list[0].position = np.array(
                [d * np.sin(self.InitialAngle), -d * np.cos(self.InitialAngle), 0])

    def collision_detection(self):
        for i in range(self.NUM_BALLS-1):
            if np.linalg.norm(self.particles_list[i].position - self.particles_list[i + 1].position) <= (
                    self.particles_list[i].radius + self.particles_list[i + 1].radius):
                for j in range(3):
                    m1 = self.particles_list[i].mass  # Mass of Fist ball in Kg
                    m2 = self.particles_list[i + 1].mass  # Mass of Second ball in Kg
                    u1 = self.particles_list[i].velocity[j]  # Initial Velocity of first ball in m/s
                    u2 = self.particles_list[i + 1].velocity[j]  # Initial Velocity of second ball in m/s
                    mu1 = m1 / 2  # Half mass used in Kinetic energy EQN
                    mu2 = m2 / 2  # Half mass used in Kinetic energy EQN
                    mr = m2 / m1  # Ratio of the two masses
                    a = (mu2 + mu1 * mr ** 2)
                    b = (-2 * mr * mu1 * u1 - 2 * u2 * (mr ** 2) * mu1 * u2 * mr ** 2)
                    c = 2 * mr * u1 * mu1 * u2 + mu1 * (mr ** 2) * (u2 ** 2) - mu2 * u2
                    self.particles_list[i + 1].velocity[j] = (-b + np.sqrt(
                        (b ** 2) - 4 * a * c)) / 2 * a  # Quadratic formula
                    self.particles_list[i].velocity[j] = u1 + mr * (u2 - self.particles_list[i + 1].velocity[j])

    def movement(self):
        for i in range(self.NUM_BALLS):
            equilibrium = np.array([self.Positioningx[i], -self.CHAIN_LENGTH, 0])
            g = np.linalg.norm(self.g)
            cosangle = np.dot(self.particles_list[i].position, equilibrium) / (
                    np.linalg.norm(self.particles_list[i].position) * np.linalg.norm(equilibrium))
            angle = np.arccos(cosangle)

            if self.particles_list[i].position[0] < self.Positioningx[i]:
                # If the particle is to the left of the equilibrium, use positive acceleration
                self.particles_list[i].acceleration = np.array([ g * np.sin(angle) * np.cos(angle),
                                                                -g * np.sin(angle) * np.sin(angle),
                                                                 0])

            if self.particles_list[i].position[0] > self.Positioningx[i]:
                # If the particle is to the right of the equilibrium, use negative acceleration
                self.particles_list[i].acceleration = np.array([-g * np.sin(angle) * np.cos(angle),
                                                                 g * np.sin(angle) * np.sin(angle),
                                                                 0])

    def FOTIerror(self):
        for i in range(self.NUM_BALLS):
            if np.linalg.norm(self.particles_list[i].position) > 2 * np.linalg.norm(
                    [self.Positioningx[i], -self.CHAIN_LENGTH, 0]):
                raise Exception("Particle flew off to infinity")

    def Period(self):
        P= 2 * np.pi * np.sqrt(self.CHAIN_LENGTH/np.linalg.norm(self.g))
        return P

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
            radius=self.radius
        )]
        super().__init__(self.particles_list, self.length, self.InitialAngle)
