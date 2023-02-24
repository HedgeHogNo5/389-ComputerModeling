import pygame
import math

# Define Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 25
NUM_BALLS = 5
BALL_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
CHAIN_COLOR = (150, 150, 150)
CHAIN_LENGTH = 150
BALL_MASS = 1


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
            G=6.67408e-11
    ):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.G = G

    """Defining the names and other variables of the Particle"""

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    """This updates the position of any body passed through this class using using the Euler-Cromer Numerical method"""

    def Euler(self, deltaT):
        self.position = self.position + self.velocity * deltaT
        self.velocity = self.velocity + self.acceleration * deltaT

    """This updates the position of any body passed through this class using using the Euler-Cromer Numerical method"""

    def EulerCromer(self, deltaT):
        self.velocity = self.velocity + self.acceleration * deltaT
        self.position = self.position + self.velocity * deltaT


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

    def draw(self, surface):
        for ball in self.balls:
            ball.draw(surface)
        pygame.draw.line(surface, CHAIN_COLOR, (self.x, self.y), (self.balls[0].x, self.balls[0].y), 2)
        pygame.draw.line(surface, CHAIN_COLOR, (self.x + (NUM_BALLS - 1) * (BALL_RADIUS * 2 + CHAIN_LENGTH), self.y),
                         (self.balls[-1].x, self.balls[-1].y), 2)
        for i in range(NUM_BALLS - 1):
            start_ball = self.balls[i]
            end_ball = self.balls[i + 1]
            pygame.draw.line(surface, CHAIN_COLOR, (start_ball.x, start_ball.y), (end_ball.x, end_ball.y), 2)

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




