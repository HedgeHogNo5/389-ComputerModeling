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
            name='Ball',  # name of the object, duhh
            mass=1.0,  # Currently in Kilograms (Kg)
            g = 9.81
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.balls = []
        for i in range(NUM_BALLS):
            ball_x = x + i * (BALL_RADIUS * 2 + CHAIN_LENGTH)
            ball_y = y + CHAIN_LENGTH
            ball = Ball(ball_x, ball_y)
            self.balls.append(ball)


    def update(self, time_step):
        for ball in self.balls:
            ball.move(time_step)
        for i in range(NUM_BALLS - 1):
            ball1 = self.balls[i]
            ball2 = self.balls[i + 1]
            distance = math.sqrt((ball2.x - ball1.x) ** 2 + (ball2.y - ball1.y) ** 2)
            if distance < BALL_RADIUS * 2:
                ball1.velocity, ball2.velocity = ball2.velocity, ball1.velocity

    def reset(self):
        for ball in self.balls:
            ball.y = self.y + CHAIN_LENGTH
            ball.velocity = 0




