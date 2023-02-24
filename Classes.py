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
GRAVITY = 9.81
BALL_MASS = 1


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.mass = BALL_MASS

    def draw(self, surface):
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)

    def move(self, time_step):
        self.y += self.velocity * time_step
        self.velocity += GRAVITY * time_step


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




